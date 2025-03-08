from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.shared.infrastructure.http.routes import base_router

app = FastAPI(
    title="SyncLife API",
    description="This is the API that contains all of SyncLife's business logic.",
    version="0.0.1",
    contact={
        "name": "SyncLife Support",
        "email": "support@synclife.com",
    },
    docs_url="/api/docs/swagger",
    redoc_url="/api/docs/redoc",
    openapi_url="/api/docs/openapi.json",
    # swagger_ui_init_oauth={
    #     "clientId": "tu_client_id",
    #     "clientSecret": "tu_client_secret",
    #     "realm": "tu_realm",
    #     "appName": "nombre_de_tu_app",
    #     "scopeSeparator": " ",
    #     "additionalQueryStringParams": {"test": "hello"}
    # }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # Permite todos los orígenes, pero en producción deberías restringirlo
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todas las cabeceras
)

app.include_router(base_router, prefix="/api")
