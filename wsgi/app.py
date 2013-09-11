import os
import inspect
import logging
import datetime
import collections

import redis
import bottle
import msgpack
import pygments
from pygments import lexers
from pygments import styles
from pygments import formatters

ROOT_DIR = os.getcwd()
BASE_DIR = os.path.join(ROOT_DIR, 'wsgi')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
VIEWS_DIR = os.path.join(BASE_DIR, 'views')
bottle.TEMPLATE_PATH.insert(0, VIEWS_DIR)

DEFAULT_FONT = 'monospace'
DEFAULT_SIZE = '10'
DEFAULT_STYLE = 'monokai'
DEFAULT_THEME = 'cyborg'

CSS_CLASS = 'source'
CODE = inspect.getsource(collections.namedtuple)

FONTS = ['Consolas', 'Droid Sans Mono', 'Source Code Pro', 'Ubuntu Mono',
    'Inconsolata', 'Anonymous Pro', 'monospace', 'Liberation Mono',
    'DejaVu Sans Mono', 'Envy Code R', 'Bitstream Vera Sans Mono']
# 'menlo', 'monaco', 'pragmata pro'

THEMES = ['cyborg', 'slate', 'amelia', 'cerulean', 'cosmo', 'flatly',
    'journal', 'readable', 'simplex', 'spacelab', 'united']

log = logging.getLogger('font')
application = bottle.default_app()

# stats
redis_args = {}
REDIS_ENV = {'HTTP_USER_AGENT', 'HTTP_COOKIE', 'HTTP_ACCEPT_LANGUAGE'}

def rconnect():
    return redis.StrictRedis(**redis_args)

@bottle.get('/static/<path:path>')
def static(path):
    log.debug('static: %s', path)
    return bottle.static_file(path, root=STATIC_DIR)

@bottle.get('/favicon.ico')
def favicon():
    return bottle.abort(404)

@bottle.get('/robots.txt')
def robots():
    return bottle.static_file('robots.txt', root=STATIC_DIR)

@bottle.get('/')
@bottle.view('index')
def index():
    r = rconnect()
    ip = bottle.request['REMOTE_ADDR']
    
    # count unique visits
    dt = datetime.datetime.now()
    r.sadd('fv:visits:{:%Y-%m-%d}'.format(dt), ip)
    
    # grab env
    env = {k: v for k, v in bottle.request.environ.items() if k in REDIS_ENV}
    r.hset('fv:env', ip, msgpack.dumps(env))
    
    # get arguments
    query = bottle.request.query
    font = query.get('font', DEFAULT_FONT).strip()
    size = query.get('size', DEFAULT_SIZE).strip()
    style = query.get('style', DEFAULT_STYLE).strip()
    theme = query.get('theme', DEFAULT_THEME).strip()
    
    # log permatheme
    r.hincrby('fv:themes', '{}_{}_{}-{}'.format(font, size, style, theme))
    
    # output
    lexer = lexers.get_lexer_by_name("python", stripall=True)
    formatter = formatters.HtmlFormatter(cssclass=CSS_CLASS)
    output = pygments.highlight(CODE, lexer, formatter)
    return {
        'code': output,
        'font': font,
        'size': size,
        'style': style,
        'theme': theme,
        'fonts': FONTS,
        'styles': styles.get_all_styles(),
        'themes': THEMES,
        }

@bottle.get('/style/<style>')
def style(style):
    bottle.response.headers['content-type'] = 'text/css'
    formatter = formatters.HtmlFormatter(cssclass=CSS_CLASS, style=style)
    return formatter.get_style_defs()

def run(debug=False):
    if debug:
        import sys
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
        redis_args = {'host': 'localhost'}
    else:
        redis_args = {'unix_socket_path': '/tmp/redis.sock'}
    
    bottle.run(host='localhost', port=22344, server='waitress',
        reloader=debug, debug=debug)

if __name__ == '__main__':
    run(debug=True)
