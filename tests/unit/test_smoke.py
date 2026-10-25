"""Smoke test: verify the package is importable and exposes a version."""

from embedai import __version__


def test_version_is_set() -> None:
    """The package version should be a non-empty string."""
    assert isinstance(__version__, str)
    assert __version__ != ""
