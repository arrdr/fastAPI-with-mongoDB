from typing import Optional
from pydantic import BaseModel, Field

class AccountSchema(BaseModel):
    # user_id: str = Field(...)  
    name: str = Field(...)
    username: str = Field(...)
    password: str = Field(...)
    team: str = Field(...)
    is_short_term: bool = Field(...)
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    education: Optional[str] = None
    is_helpdesk: bool = Field(...)
    is_admin: Optional[bool] = False

    class Config:
        json_schema_extra = {
            "example": {
                # "user_id": "USER123",  # Add example
                "name": "John Doe",
                "username": "johndoe",
                "password": "secretpass123",
                "team": "Development",
                "is_short_term": False,
                "start_date": "2025-02-17",
                "end_date": "2026-02-17",
                "education": "Computer Science",
                "is_helpdesk": False,
                "is_admin": False
            }
        }

class UpdateAccountModel(BaseModel):
    name: Optional[str]
    password: Optional[str]
    team: Optional[str]
    is_short_term: Optional[bool]
    start_date: Optional[str]
    end_date: Optional[str]
    education: Optional[str]
    is_helpdesk: Optional[bool]
    is_admin: Optional[bool]

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe Updated",
                "team": "Support",
                "is_helpdesk": True
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
