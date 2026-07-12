"""Unit tests for example/print."""

from logot import Logot, logged
from typer.testing import CliRunner

from {{ cookiecutter.underscore }}.main import app

runner = CliRunner(mix_stderr=False)


def test_example_test_print(logot: Logot) -> None:
    """Test example print-test."""
    result = runner.invoke(app, ["example", "test-print"])
    assert result.exit_code == 0
    assert result.stdout == "Example\n"
    logot.assert_logged(logged.info("Info message"))


def test_example_test_print_debug_flag(logot: Logot) -> None:
    """Test --debug example print-test."""
    result = runner.invoke(app, ["--debug", "example", "test-print"])
    assert result.exit_code == 0
    assert result.stdout == "Example\n"
    logot.assert_logged(logged.debug("Debug message"))
    logot.assert_logged(logged.info("Info message"))
