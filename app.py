#!/usr/bin/env python
import imp
import os

try:
   zvirtenv = os.path.join(os.environ['OPENSHIFT_PYTHON_DIR'],
                           'virtenv', 'bin', 'activate_this.py')
   exec(compile(open(zvirtenv).read(), zvirtenv, 'exec'),
        dict(__file__ = zvirtenv) )
except IOError:
   pass

def run_waitress_server(app, ip, port=8080):
   import waitress
   waitress.serve(app, host=ip, port=port)

def run_simple_httpd_server(app, ip, port=8080):
   from wsgiref.simple_server import make_server
   make_server(ip, port, app).serve_forever()

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

#
#  main():
#
if __name__ == '__main__':
    from wsgi.app import application
    
    ip   = os.environ['OPENSHIFT_PYTHON_IP']
    port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
    
    print('Starting server on %s:%d ... ' % (ip, port))
    try:
        run_waitress_server(application, ip, port)
    except Exception:
        print("could not load waitress - using default simple server ...")
        run_simple_httpd_server(application, ip, port)
