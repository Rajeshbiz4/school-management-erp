# School ERP Python Backend Boilerplate

Python FastAPI backend boilerplate for a School/College ERP project.

## Included Modules

- Employee Management
- Maintenance Ticket Management
- Dashboard Reports
- In-memory local database for beginner execution
- Azure Cosmos DB repository support for cloud database
- Swagger API docs
- Basic test setup

## Quick Start on Windows

```bash
setup_windows.bat
run.bat
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Manual Start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

## API Endpoints

```text
GET    /health
GET    /api/v1/employees
POST   /api/v1/employees
GET    /api/v1/employees/{employee_id}
PUT    /api/v1/employees/{employee_id}
DELETE /api/v1/employees/{employee_id}

GET    /api/v1/maintenance
POST   /api/v1/maintenance
GET    /api/v1/maintenance/{ticket_id}
PUT    /api/v1/maintenance/{ticket_id}
DELETE /api/v1/maintenance/{ticket_id}

GET    /api/v1/reports/dashboard
```

## Cosmos DB Mode

By default, `.env.example` uses:

```env
USE_IN_MEMORY_DB=true
```

To use Azure Cosmos DB, set:

```env
USE_IN_MEMORY_DB=false
COSMOS_ENDPOINT=your-endpoint
COSMOS_KEY=your-key
```

Read `BACKEND_SETUP_STEPS.md` for complete beginner setup.
