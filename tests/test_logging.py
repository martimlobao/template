"""Tests for foobar.core.logging."""

from foobar.core.logging import setup_logging


def test_setup_logging() -> None:
    """setup_logging configures the root logger without raising."""
    setup_logging()  # Idempotent; may already be configured by other modules
