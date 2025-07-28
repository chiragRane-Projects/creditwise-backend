from fastapi import FastAPI
from app.api.v1 import user_routes

app = FastAPI(
    title="CreditWise API",
    version="1.0.0"
)

app.include_router(user_routes.router, prefix="/api/v1/user", tags=["User"])