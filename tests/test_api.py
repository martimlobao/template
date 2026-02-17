"""Tests for foobar.api.main."""

import runpy
import warnings
from unittest.mock import patch

from fastapi.testclient import TestClient

from foobar.api.main import app, main


def test_health() -> None:
    """Health endpoint returns ok status."""
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_main() -> None:
    """Main() runs uvicorn with api_config."""
    with patch("foobar.api.main.uvicorn.run") as run:
        main()
    run.assert_called_once()
    call_kwargs = run.call_args.kwargs
    assert call_kwargs["host"] == "localhost"
    assert call_kwargs["port"] == 8000
    assert call_kwargs["reload"] is True


def test_main_entry_point() -> None:
    """Running api.main as __main__ invokes main()."""
    with patch("uvicorn.run"), warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        runpy.run_module("foobar.api.main", run_name="__main__")
