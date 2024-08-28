from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str = Field(min_length=6, max_length=20)

class UserCreate(UserBase):
    # минимум 8 символов, хотя бы 1 маленькую и 1 большую буквы и хотя бы 1 цифру
    password: str = Field(
        min_length=8, 
        max_length=32
    )

class User(UserBase):
    id: int

class UserLogin(BaseModel):
    username: str = Field(
        min_length=6, 
        max_length=20
    )
    password: str = Field(
        min_length=8,
        max_length=32
    )