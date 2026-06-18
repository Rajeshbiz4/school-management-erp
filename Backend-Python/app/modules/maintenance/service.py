from datetime import datetime, timezone
from typing import List, Optional

from app.core.config import get_settings
from app.db.repository import BaseRepository
from app.modules.maintenance.schemas import MaintenanceTicket, MaintenanceTicketCreate, MaintenanceTicketUpdate


class MaintenanceService:
    def __init__(self) -> None:
        self.repository = BaseRepository(get_settings().cosmos_maintenance_container)

    def list_tickets(self) -> List[dict]:
        return self.repository.list_items()

    def get_ticket(self, ticket_id: str) -> Optional[dict]:
        return self.repository.get_item(ticket_id)

    def create_ticket(self, payload: MaintenanceTicketCreate) -> dict:
        ticket = MaintenanceTicket.from_create(payload)
        return self.repository.upsert_item(ticket.model_dump(mode="json"))

    def update_ticket(self, ticket_id: str, payload: MaintenanceTicketUpdate) -> Optional[dict]:
        existing = self.repository.get_item(ticket_id)
        if not existing:
            return None

        existing.update(payload.model_dump(exclude_unset=True))
        existing["updated_at"] = datetime.now(timezone.utc).isoformat()
        return self.repository.upsert_item(existing)

    def delete_ticket(self, ticket_id: str) -> bool:
        return self.repository.delete_item(ticket_id)
