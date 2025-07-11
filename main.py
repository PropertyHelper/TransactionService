import uvicorn
from src.api.v1.app import build_app
from src.container import Container

if __name__ == '__main__':
    container = Container()
    container.config.db_url.from_env("db_connection_str", required=True)

    app = build_app(container)

    uvicorn.run(app, port=8003, host="0.0.0.0")
