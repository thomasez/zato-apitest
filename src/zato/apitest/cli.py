# -*- coding: utf-8 -*-

"""
Copyright (C) 2014 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# Originally part of Zato - open-source ESB, SOA, REST, APIs and cloud integrations in Python
# https://zato.io

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
import os, sys, tempfile, uuid

# Click
import click

# Zato
from zato.apitest import init as _init, run as _run

@click.group()
def main():
    pass

def cli_init(ctx, path, prompt_run=True):
    if os.path.exists(path) and os.listdir(path):
        click.echo(ctx.get_help())
        click.echo('\nError: directory `{}` is not empty, quitting.'.format(path))
        sys.exit(1)

    if not os.path.exists(path):
        click.echo('Creating directory `{}`.'.format(path))
        os.makedirs(path)

    _init.handle(path)
    click.echo('OK, initialized.')

    if prompt_run:
        click.echo('Run `apitest run {}` for a live demo.'.format(path))

@click.command()
@click.argument('path', type=click.Path(exists=False, file_okay=False, resolve_path=True))
@click.pass_context
def init(ctx, path):
    cli_init(ctx, path)

@click.command()
@click.argument('path', type=click.Path(exists=True, file_okay=False, resolve_path=True))
@click.option('-b', '--behave-options', help='Override options to behave.')
def run(path, behave_options):
    _run.handle(path, behave_options)

@click.command()
@click.argument('path', default=tempfile.gettempdir(), type=click.Path(exists=True, file_okay=False, resolve_path=True))
@click.pass_context
def demo(ctx, path):
    # We're not using tempfile.mkdtemp because we may as well be run
    # in a user-provided directory.
    path = os.path.join(path, uuid.uuid4().hex)
    cli_init(ctx, path, False)
    _run.handle(path)

main.add_command(init)
main.add_command(run)
main.add_command(demo)

if __name__ == '__main__':
    main()
