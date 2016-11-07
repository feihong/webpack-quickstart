import os
from invoke import task


@task
def serve(ctx):
    import http.server
    import socketserver

    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(('localhost', 8000), Handler)
    print('Serving on localhost:8000')
    os.chdir('static')
    httpd.serve_forever()


@task
def build(ctx):
    ctx.run('webpack --progress --colors --optimize-minimize')


@task
def watch(ctx):
    ctx.run('webpack --progress --colors --debug --watch')
