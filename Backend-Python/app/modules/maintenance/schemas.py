from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, Field


class MaintenanceTicketCreate(BaseModel):
    title: str = Field(..., min_length=3, examples=["Classroom fan not working"])
    description: str = Field(..., min_length=5)
    category: str = Field(default="General", examples=["Electrical"])
    priority: str = Field(default="medium", examples=["low", "medium", "high"])
    assigned_to: Optional[str] = None
    status: str = Field(default="open", examples=["open", "in_progress", "closed"])


class MaintenanceTicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    priority: Optional[str] = None
    assigned_to: Optional[str] = None
    status: Optional[str] = None


class MaintenanceTicket(MaintenanceTicketCreate):
    id: str
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_create(payload: MaintenanceTicketCreate) -> "MaintenanceTicket":
        now = datetime.now(timezone.utc)
        return MaintenanceTicket(id=str(uuid4()), created_at=now, updated_at=now, **payload.model_dump())
