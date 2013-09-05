import os
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

CODE = """for i in range(10):
    print "test" * i
"""

FONTS = ['consolas', 'menlo', 'droid sans mono', 'source code pro',
    'ubuntu mono']

THEMES = ['cyborg', 'slate', 'amelia', 'cerulean', 'cosmo', 'flatly',
    'journal', 'readable', 'simplex', 'spacelab', 'united']

application = bottle.default_app()

@bottle.get('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root=STATIC_DIR)

@bottle.get('/favicon.ico')
def favicon():
    return bottle.abort(404)

@bottle.get('/')
@bottle.view('index')
def index():
    lexer = lexers.get_lexer_by_name("python", stripall=True)
    formatter = formatters.HtmlFormatter(
        linenos=True, cssclass="source", style="monokai")
    output = pygments.highlight(CODE, lexer, formatter)
    return {
        'code': output,
        'style': formatter.get_style_defs(),
        'fonts': FONTS,
        'styles': styles.get_all_styles(),
        'themes': THEMES,
        }

def run():
    bottle.run(host='localhost', port=22344, server='waitress',
        reloader=True, debug=True)

if __name__ == '__main__':
    run()
