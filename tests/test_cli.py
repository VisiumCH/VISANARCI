"""Tests for the ANARCI command-line interface."""
import subprocess


def test_anarci_cli_help():
    result = subprocess.run(
        ["ANARCI", "-h"],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "ANARCI" in result.stdout