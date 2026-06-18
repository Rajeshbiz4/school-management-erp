from datetime import datetime, timezone
from typing import List, Optional

from app.core.config import get_settings
from app.db.repository import BaseRepository
from app.modules.employees.schemas import Employee, EmployeeCreate, EmployeeUpdate


class EmployeeService:
    def __init__(self) -> None:
        self.repository = BaseRepository(get_settings().cosmos_employee_container)

    def list_employees(self) -> List[dict]:
        return self.repository.list_items()

    def get_employee(self, employee_id: str) -> Optional[dict]:
        return self.repository.get_item(employee_id)

    def create_employee(self, payload: EmployeeCreate) -> dict:
        employee = Employee.from_create(payload)
        return self.repository.upsert_item(employee.model_dump(mode="json"))

    def update_employee(self, employee_id: str, payload: EmployeeUpdate) -> Optional[dict]:
        existing = self.repository.get_item(employee_id)
        if not existing:
            return None

        update_data = payload.model_dump(exclude_unset=True)
        existing.update(update_data)
        existing["updated_at"] = datetime.now(timezone.utc).isoformat()
        return self.repository.upsert_item(existing)

    def delete_employee(self, employee_id: str) -> bool:
        return self.repository.delete_item(employee_id)
