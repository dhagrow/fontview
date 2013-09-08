import os
import inspect
import collections

import bottle
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
DEFAULT_SIZE = 10
DEFAULT_STYLE = 'monokai'
DEFAULT_THEME = 'cyborg'

CSS_CLASS = 'source'
CODE = inspect.getsource(collections.namedtuple)

FONTS = ['consolas', 'droid sans mono', 'source code pro', 'ubuntu mono',
    'inconsolata', 'anonymous pro', 'monospace']
# 'dejavu sans mono', 'envy code r', 'menlo', 'monaco', 'pragmata pro'

THEMES = ['cyborg', 'slate', 'amelia', 'cerulean', 'cosmo', 'flatly',
    'journal', 'readable', 'simplex', 'spacelab', 'united']

application = bottle.default_app()

@bottle.get('/static/<path:path>')
def static(path):
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
    query = bottle.request.query
    font = query.get('font', DEFAULT_FONT).strip()
    size = query.get('size', DEFAULT_SIZE).strip()
    style = query.get('style', DEFAULT_STYLE).strip()
    theme = query.get('theme', DEFAULT_THEME).strip()
    
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
    bottle.run(host='localhost', port=22344, server='waitress',
        reloader=debug, debug=debug)

if __name__ == '__main__':
    run(debug=True)
