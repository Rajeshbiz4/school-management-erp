from fastapi import APIRouter, HTTPException, status

from app.common.response import success
from app.modules.employees.schemas import EmployeeCreate, EmployeeUpdate
from app.modules.employees.service import EmployeeService

router = APIRouter(prefix="/employees", tags=["Employees"])
service = EmployeeService()


@router.get("")
def list_employees():
    return success(service.list_employees())


@router.get("/{employee_id}")
def get_employee(employee_id: str):
    employee = service.get_employee(employee_id)
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return success(employee)


@router.post("", status_code=status.HTTP_201_CREATED)
def create_employee(payload: EmployeeCreate):
    return success(service.create_employee(payload), "Employee created successfully")


@router.put("/{employee_id}")
def update_employee(employee_id: str, payload: EmployeeUpdate):
    employee = service.update_employee(employee_id, payload)
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return success(employee, "Employee updated successfully")


@router.delete("/{employee_id}")
def delete_employee(employee_id: str):
    deleted = service.delete_employee(employee_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return success({"id": employee_id}, "Employee deleted successfully")
