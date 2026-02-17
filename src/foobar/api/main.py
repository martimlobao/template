import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from foobar.core.config import api_config
from foobar.core.logging import setup_logging

setup_logging()

app: FastAPI = FastAPI(title=api_config.app_name)

app.add_middleware(
    CORSMiddleware,  # type: ignore[reportCallIssue]
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
    """Return a simple health status payload."""
    return {"status": "ok"}


def main() -> None:
    uvicorn.run(
        f"{__name__}:app",
        host=api_config.host,
        port=api_config.port,
        reload=api_config.reload,
    )


if __name__ == "__main__":
    main()
