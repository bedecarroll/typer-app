"""Version tests."""

from typer.testing import CliRunner

from {{ cookiecutter.underscore }}.main import app

runner = CliRunner()


def test_version_subcommand() -> None:
    """Test version."""
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert result.stdout == "0.0.1\n"
