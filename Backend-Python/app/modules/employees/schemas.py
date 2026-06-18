from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, EmailStr, Field


class EmployeeCreate(BaseModel):
    first_name: str = Field(..., min_length=2, examples=["Rohit"])
    last_name: str = Field(..., min_length=2, examples=["Sharma"])
    email: EmailStr
    mobile: Optional[str] = None
    department: str = Field(default="Administration")
    designation: str = Field(default="Staff")
    status: str = Field(default="active", examples=["active"])


class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    mobile: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    status: Optional[str] = None


class Employee(EmployeeCreate):
    id: str
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_create(payload: EmployeeCreate) -> "Employee":
        now = datetime.now(timezone.utc)
        return Employee(id=str(uuid4()), created_at=now, updated_at=now, **payload.model_dump())
