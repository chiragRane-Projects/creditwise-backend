from fastapi import FastAPI
from app.api.v1 import route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="CreditWise API",
    version="1.0.0"
)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost",  # if you're using something else
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # 👈 Allow frontend dev origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(route.router, prefix="/api/v1/user", tags=["User"])