"""{{ cookiecutter.name }} entrypoint."""

import sys
from typing import Annotated

import typer
from icecream import install  # pyright: ignore[reportMissingTypeStubs]
from loguru import logger

from {{ cookiecutter.underscore }}.example import app as example_app
from {{ cookiecutter.underscore }}.version import app as version_app
from {{ cookiecutter.underscore }}.version import version_callback

app = typer.Typer(
    context_settings={"help_option_names": ["-h", "--help"]}, no_args_is_help=True
)
app.add_typer(example_app, name="example")
app.add_typer(version_app)


@app.callback(invoke_without_command=True)
def main(
    debug: Annotated[
        bool | None, typer.Option("--debug", help="Enable debug logging.")
    ] = None,
    version: Annotated[  # noqa: ARG001 # pyright: ignore[reportUnusedParameter]
        bool | None,
        typer.Option(
            "--version",
            "-V",
            help="Print version.",
            callback=version_callback,
            is_eager=True,
        ),
    ] = None,
) -> None:
    """{{ cookiecutter.name|capitalize }} CLI tool."""
    install()
    if not debug:
        try:
            ic.disable()  # noqa: F821 # pyright: ignore[reportUnknownMemberType,reportUndefinedVariable]
            logger.remove(0)
            _ = logger.add(sys.stderr, level="INFO")
        except ValueError:
            # NOTE: this is to fix unit tests removing the handler multiple times
            logger.debug("Already set to debug level, skipping remove")


if __name__ == "__main__":
    app()
