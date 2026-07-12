"""Version."""

from importlib.metadata import version as ver

import typer

app = typer.Typer()


def version_callback(version: bool) -> None:  # noqa: FBT001
    """Print version in metadata and quit."""
    if version:
        typer.echo(ver("{{ cookiecutter.underscore }}"))
        raise typer.Exit


@app.command()
def version() -> None:
    """Print version and quit."""
    version_callback(version=True)
