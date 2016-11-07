from invoke import task, run


@task
def serve(ctx):
    run('python -m SimpleHTTPServer 8000')


@task
def build(ctx):
    run('webpack --progress --colors --optimize-minimize')


@task
def watch(ctx):
    run('webpack --progress --colors -d --watch')
