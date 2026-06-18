from fastapi import APIRouter

from app.common.response import success
from app.modules.employees.service import EmployeeService
from app.modules.maintenance.service import MaintenanceService

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get("/dashboard")
def dashboard_report():
    employees = EmployeeService().list_employees()
    tickets = MaintenanceService().list_tickets()

    open_tickets = [ticket for ticket in tickets if ticket.get("status") != "closed"]
    active_employees = [emp for emp in employees if emp.get("status") == "active"]

    return success({
        "total_employees": len(employees),
        "active_employees": len(active_employees),
        "total_maintenance_tickets": len(tickets),
        "open_maintenance_tickets": len(open_tickets),
    })
