from invoke import task


@task
def serve(ctx):
    ctx.run('cd static; python3 -m http.server 8000')


@task
def build(ctx):
    ctx.run('webpack --progress --colors --optimize-minimize')


@task
def watch(ctx):
    ctx.run('webpack --progress --colors -d --watch')
