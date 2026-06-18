# Backend Setup Guide: Python FastAPI + Azure Cosmos DB

This guide is for beginners who want to run the School ERP backend boilerplate on a Windows system.

---

## 1. Software to Install

| Software | Why needed | Download link |
|---|---|---|
| Python 3.12 or latest stable Python 3 | Backend programming language | https://www.python.org/downloads/ |
| Visual Studio Code | Code editor | https://code.visualstudio.com/download |
| Git for Windows | Clone/push code to GitHub/GitLab | https://git-scm.com/install/windows |
| Azure Account | Required later for Cosmos DB cloud database | https://azure.microsoft.com/free/ |
| Azure Cosmos DB Emulator | Optional local Cosmos DB testing | https://learn.microsoft.com/azure/cosmos-db/emulator |
| Postman | Optional API testing tool | https://www.postman.com/downloads/ |

---

## 2. Verify Installation

Open **Command Prompt** or **PowerShell** and run:

```bash
python --version
pip --version
git --version
code --version
```

If `python --version` is not working, reinstall Python and tick this checkbox during installation:

```text
Add python.exe to PATH
```

---

## 3. Extract Boilerplate

Extract this ZIP file:

```text
school-erp-python-backend-boilerplate.zip
```

Suggested path:

```text
D:\workspace\school-erp-python-backend-boilerplate
```

Open folder in VS Code:

```bash
cd D:\workspace\school-erp-python-backend-boilerplate
code .
```

---

## 4. Create Python Virtual Environment

Run these commands inside the project folder:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

When virtual environment is active, you will see something like:

```text
(.venv) D:\workspace\school-erp-python-backend-boilerplate>
```

---

## 5. Create Environment File

Copy `.env.example` and create `.env`:

```bash
copy .env.example .env
```

For beginner/local execution, keep this value:

```env
USE_IN_MEMORY_DB=true
```

This means backend will run without Azure Cosmos DB.

---

## 6. Run Backend API

Run:

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Or simply run:

```bash
run.bat
```

Open in browser:

```text
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/health
```

---

## 7. Test First API from Swagger

Open:

```text
http://127.0.0.1:8000/docs
```

Try these APIs:

### Create Employee

```http
POST /api/v1/employees
```

Sample body:

```json
{
  "first_name": "Rohit",
  "last_name": "Sharma",
  "email": "rohit@example.com",
  "mobile": "9876543210",
  "department": "IT",
  "designation": "Developer",
  "status": "active"
}
```

### List Employees

```http
GET /api/v1/employees
```

### Create Maintenance Ticket

```http
POST /api/v1/maintenance
```

Sample body:

```json
{
  "title": "Classroom fan not working",
  "description": "Fan in classroom 101 is not working",
  "category": "Electrical",
  "priority": "medium",
  "assigned_to": "Rohit",
  "status": "open"
}
```

### Dashboard Report

```http
GET /api/v1/reports/dashboard
```

---

## 8. Enable Azure Cosmos DB Later

After you create Azure Cosmos DB account and database, update `.env`:

```env
USE_IN_MEMORY_DB=false
COSMOS_ENDPOINT=https://your-cosmos-account.documents.azure.com:443/
COSMOS_KEY=your-primary-key
COSMOS_DATABASE_NAME=school_erp_db
COSMOS_EMPLOYEE_CONTAINER=employees
COSMOS_MAINTENANCE_CONTAINER=maintenance_tickets
```

Then restart API:

```bash
uvicorn app.main:app --reload
```

---

## 9. Useful Project Commands

```bash
# Activate virtual environment
.venv\Scripts\activate

# Install dependency
pip install package-name

# Save dependency
pip freeze > requirements.txt

# Run API
uvicorn app.main:app --reload

# Run tests
pytest

# Stop server
CTRL + C
```

---

## 10. Project Folder Structure

```text
school-erp-python-backend-boilerplate/
├── app/
│   ├── api/v1/router.py
│   ├── core/config.py
│   ├── db/
│   │   ├── cosmos_client.py
│   │   ├── in_memory_store.py
│   │   └── repository.py
│   ├── modules/
│   │   ├── employees/
│   │   ├── maintenance/
│   │   └── reports/
│   └── main.py
├── tests/test_health.py
├── .env.example
├── requirements.txt
├── setup_windows.bat
├── run.bat
└── README.md
```

---

## 11. Beginner Execution Flow

1. Install Python, VS Code, and Git.
2. Extract backend ZIP.
3. Open folder in VS Code.
4. Run `setup_windows.bat`.
5. Run `run.bat`.
6. Open `http://127.0.0.1:8000/docs`.
7. Test Employee, Maintenance, and Reports APIs.
8. Later connect Azure Cosmos DB by updating `.env`.

---

## 12. Common Errors and Fixes

### Error: `python is not recognized`

Fix: Reinstall Python and select `Add python.exe to PATH`.

### Error: `No module named fastapi`

Fix:

```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

### Error: Port already in use

Run on another port:

```bash
uvicorn app.main:app --reload --port 8001
```

### Error: Cosmos DB endpoint/key missing

For beginner mode, keep:

```env
USE_IN_MEMORY_DB=true
```

Use Cosmos DB values only when your Azure account is ready.
