from fastapi import APIRouter, HTTPException, status

from app.common.response import success
from app.modules.maintenance.schemas import MaintenanceTicketCreate, MaintenanceTicketUpdate
from app.modules.maintenance.service import MaintenanceService

router = APIRouter(prefix="/maintenance", tags=["Maintenance"])
service = MaintenanceService()


@router.get("")
def list_tickets():
    return success(service.list_tickets())


@router.get("/{ticket_id}")
def get_ticket(ticket_id: str):
    ticket = service.get_ticket(ticket_id)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    return success(ticket)


@router.post("", status_code=status.HTTP_201_CREATED)
def create_ticket(payload: MaintenanceTicketCreate):
    return success(service.create_ticket(payload), "Maintenance ticket created successfully")


@router.put("/{ticket_id}")
def update_ticket(ticket_id: str, payload: MaintenanceTicketUpdate):
    ticket = service.update_ticket(ticket_id, payload)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    return success(ticket, "Maintenance ticket updated successfully")


@router.delete("/{ticket_id}")
def delete_ticket(ticket_id: str):
    deleted = service.delete_ticket(ticket_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    return success({"id": ticket_id}, "Maintenance ticket deleted successfully")
