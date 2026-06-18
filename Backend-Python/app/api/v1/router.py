from fastapi import APIRouter

from app.modules.employees.router import router as employees_router
from app.modules.maintenance.router import router as maintenance_router
from app.modules.reports.router import router as reports_router

api_router = APIRouter()
api_router.include_router(employees_router)
api_router.include_router(maintenance_router)
api_router.include_router(reports_router)
