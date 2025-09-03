from fastapi import FastAPI 
from schemas import UserCreate, User, Token, UserInDB
from utils import hash_password, verify_password
from auth_utils import create_access_token



app = FastAPI()

# In-memory "database" for MVP/testing
users_db = {}  # key: username, value: UserInDB

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://cautious-couscous-v6564494vjq4hp4x-5173.app.github.dev"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Signup
@app.post("/auth/signup", response_model=User)
def signup(user: UserCreate):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed = hash_password(user.password)
    user_in_db = UserInDB(id=len(users_db)+1, username=user.username, email=user.email, hashed_password=hashed)
    users_db[user.username] = user_in_db
    return user_in_db

# Login
@app.post("/auth/login", response_model=Token)
def login(user: UserCreate):
    db_user = users_db.get(user.username)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = create_access_token({"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}