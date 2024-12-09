from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    username: str
    email: EmailStr
    project_id: str

    class Config:
        orm_mode = True

class UpdateUser(BaseModel):
    id: str
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    project_id: Optional[str] = None

    class Config:
        orm_mode = True
