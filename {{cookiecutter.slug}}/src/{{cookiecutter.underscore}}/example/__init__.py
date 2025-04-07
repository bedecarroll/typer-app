"""Example sub-command."""

import typer

from {{ cookiecutter.underscore }}.example.print import app as print_app

app = typer.Typer(no_args_is_help=True, help="Example sub-commands.")

app.add_typer(print_app)
