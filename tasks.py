import os
import subprocess
import signal
from invoke import task


WEBPACK_WATCH_COMMAND = 'webpack --progress --colors --debug --watch'


@task
def serve(ctx):
    import http.server
    import socketserver

    webpack_proc = subprocess.Popen(WEBPACK_WATCH_COMMAND, shell=True)

    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(('localhost', 8000), Handler)
    print('Serving on localhost:8000')
    os.chdir('static')
    httpd.serve_forever()
    # Server is stopped, so stop webpack as well.
    webpack_proc.send_signal(signal.SIGINT)
    webprack_proc.wait()


@task
def build(ctx):
    ctx.run('webpack --progress --colors --optimize-minimize')


@task
def watch(ctx):
    ctx.run(WEBPACK_WATCH_COMMAND)
