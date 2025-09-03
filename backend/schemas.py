from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class User(BaseModel):
    id: int
    username: str
    email: EmailStr

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str