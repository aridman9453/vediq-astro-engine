from pydantic import BaseModel, EmailStr


class SignupRequest(BaseModel):
    email: EmailStr
    password: str
    full_name: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class BirthChartRequest(BaseModel):
    birth_date: str
    birth_time: str
    latitude: float
    longitude: float
    timezone: float
