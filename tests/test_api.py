"""Tests for foobar.api.main."""

import runpy
import warnings
from unittest.mock import patch

from httpx2 import Response
from starlette.testclient import TestClient

from foobar.api.main import app, main


def test_health() -> None:
    """Health endpoint returns ok status."""
    client = TestClient(app)
    response = client.get("/health")
    assert isinstance(response, Response)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_main() -> None:
    """Main() runs uvicorn with api_config."""

    class DummyApiConfig:
        host = "testhost"
        port = 1234
        reload = False

    with (
        patch("foobar.api.main.api_config", DummyApiConfig),
        patch("foobar.api.main.uvicorn.run") as run,
    ):
        main()
    run.assert_called_once()
    args, kwargs = run.call_args
    assert args[0] == "foobar.api.main:app"
    assert kwargs["host"] == DummyApiConfig.host
    assert kwargs["port"] == DummyApiConfig.port
    assert kwargs["reload"] == DummyApiConfig.reload


def test_main_entry_point() -> None:
    """Running api.main as __main__ invokes main()."""
    with (
        patch("uvicorn.run") as run,
        warnings.catch_warnings(),
    ):
        warnings.simplefilter("ignore", RuntimeWarning)
        runpy.run_module("foobar.api.main", run_name="__main__")
    run.assert_called_once()
