from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    
class UserOut(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    user_type: str
    
    class Config:
        orm_mode = True
        
class UserLogin(BaseModel):
    email : EmailStr
    password: str