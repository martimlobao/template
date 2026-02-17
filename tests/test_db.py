"""Tests for foobar.db.schema."""

from unittest.mock import MagicMock, patch

from foobar.db.schema import Base, get_db


def test_base_declarative_base() -> None:
    """Base is a DeclarativeBase subclass."""
    assert hasattr(Base, "metadata")


def test_get_db_yields_and_closes_session() -> None:
    """get_db yields a session and closes it on exit."""
    mock_session = MagicMock()
    with patch("foobar.db.schema.SessionLocal", return_value=mock_session):
        sessions = list(get_db())
    assert sessions == [mock_session]
    mock_session.close.assert_called_once()
