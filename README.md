# Student Management API

A small REST API built with Python and FastAPI for creating, retrieving, filtering, updating, and deleting student records, with marks-based search and academic summary endpoints.

> **Storage note:** This learning project currently stores records in a Python list. Data resets when the application process restarts. It is not a persistent database application.

## Features

- Create, read, replace, update, and delete student records
- Retrieve records with offset/limit pagination
- Filter students by department
- Search students using a minimum marks threshold
- Calculate student count and average marks
- Validate names, departments, marks, and pagination parameters
- Return appropriate HTTP status codes for missing records and invalid requests
- Automatic Swagger UI and OpenAPI documentation

## Technology stack

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn
- pytest and HTTPX

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/kirubanandhan016/Student-Management-API.git
cd Student-Management-API
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the API

```bash
uvicorn main:app --reload
```

- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/students` | Create a student |
| GET | `/students` | List students; supports `offset` and `limit` |
| GET | `/students/{student_id}` | Retrieve one student |
| PUT | `/students/{student_id}` | Replace a student record |
| PATCH | `/students/{student_id}` | Update selected fields |
| DELETE | `/students/{student_id}` | Delete a student |
| GET | `/filter-students?department=ECE` | Filter by department |
| GET | `/students/search/by-marks?min_marks=80` | Find students at or above a marks threshold |
| GET | `/summary` | Return student count and average marks |

### Create a student

```bash
curl -X POST http://127.0.0.1:8000/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Meena","department":"ECE","marks":88}'
```

Example response:

```json
{
  "id": 4,
  "name": "Meena",
  "department": "ECE",
  "marks": 88
}
```

### Update marks

```bash
curl -X PATCH http://127.0.0.1:8000/students/4 \
  -H "Content-Type: application/json" \
  -d '{"marks":91}'
```

### Filter by department

```bash
curl "http://127.0.0.1:8000/filter-students?department=ECE"
```

## Run tests

```bash
python -m pytest -v
```

The tests use the in-memory application data and do not require a database service.

## Project structure

```text
Student-Management-API/
├── main.py
├── tests/
│   ├── conftest.py
│   └── test_students.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── .gitignore
├── requirements.txt
└── README.md
```

## Future improvements

- Persist records using PostgreSQL or SQLite
- Introduce SQLAlchemy models and Alembic migrations
- Add authentication and role-based authorization if multiple user roles are introduced
- Add structured logging and deployment configuration

## Author

**Kirubanandhan V**

- GitHub: https://github.com/kirubanandhan016
- LinkedIn: https://www.linkedin.com/in/kirubanandhan-v-98bb83443/
