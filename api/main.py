from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from db import session
from models.User import Users



app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3000/ceos",
    "http://localhost:5173",
    "http://localhost:5174"
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {"message: root route."}

@app.get("/users")
def get_users():
    user = session.query(Users)
    return user.all()