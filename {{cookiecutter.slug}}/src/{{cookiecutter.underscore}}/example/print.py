"""Example sub-command."""

import typer
from loguru import logger

app = typer.Typer()


@app.command()
def test_print() -> None:
    """."""
    ic("ic example")  # noqa: F821 # pyright: ignore[reportUndefinedVariable]
    logger.debug("Debug message")
    logger.info("Info message")
    typer.echo("Example")
