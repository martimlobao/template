"""Tests for foobar.core.config."""

import pytest

from foobar.core.config import ApiConfig, DBConfig


def test_api_config_defaults() -> None:
    """Default values are correct."""
    config = ApiConfig()
    assert config.app_name == "Foobar"
    assert config.host == "localhost"
    assert config.port == 8000
    assert config.environment == "development"


def test_api_config_reload_true_in_development() -> None:
    """Reload is True when environment is development."""
    config = ApiConfig(environment="development")
    assert config.reload is True


def test_api_config_reload_false_in_production() -> None:
    """Reload is False when environment is production."""
    config = ApiConfig(environment="production")
    assert config.reload is False


def test_db_config_default_db_url() -> None:
    """Default database URL is set."""
    config = DBConfig()
    assert "postgresql" in config.db_url
    assert config.scheme in {"postgresql", "postgresql+psycopg"}
    assert config.host == "localhost"
    assert config.user == "user"
    assert config.password == "password"  # noqa: S105
    assert config.port == 5432


def test_db_config_url_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """Database URL can be overridden via env."""
    monkeypatch.setenv(
        "DATABASE_URL",
        "postgresql+psycopg://test:secret@db.example.com:5433/mydb",
    )
    config = DBConfig()
    assert "test" in config.db_url
    assert "db.example.com" in config.db_url
    assert config.host == "db.example.com"
    assert config.user == "test"
    assert config.password == "secret"  # noqa: S105
    assert config.port == 5433
