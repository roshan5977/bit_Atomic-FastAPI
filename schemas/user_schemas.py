from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str
    is_active: bool
    role: str


class UserCreate(UserBase):
    password: str
    created_by: str
    updated_by: str


class Email(BaseModel):
    to_email: str
    subject: str
    body: str


class UserLogin(BaseModel):
    email: str
    password: str




class User(UserBase):
    id: int

    class Config:
        orm_mode = True
