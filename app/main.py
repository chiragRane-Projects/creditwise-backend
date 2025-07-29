from fastapi import FastAPI
from app.api.v1 import route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="CreditWise API",
    version="1.0.0"
)

# origins = [
#     "https://creditwise-rouge.vercel.app",
#     "http://localhost:3000"
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(route.router, prefix="/api/v1/user", tags=["User"])