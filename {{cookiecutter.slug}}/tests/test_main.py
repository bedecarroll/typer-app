"""Unit tests for main commands."""

from typer.testing import CliRunner

from {{ cookiecutter.underscore }}.main import app

runner = CliRunner()


def test_main_version_flag() -> None:
    """Test -V."""
    result = runner.invoke(app, ["-V"])
    assert result.exit_code == 0
    assert result.stdout == "0.0.1\n"


def test_main_debug_flag() -> None:
    """Test --debug."""
    result = runner.invoke(app, ["--debug"])
    assert result.exit_code == 0
