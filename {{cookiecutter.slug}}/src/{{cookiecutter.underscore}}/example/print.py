"""Example sub-command."""

import typer
from loguru import logger

app = typer.Typer()


@app.command()
def test_print() -> None:
    """."""
    logger.debug("Debug message")
    logger.info("Info message")
    typer.echo("Example")
