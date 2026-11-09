# Student Management API

[![API tests](https://github.com/kirubanandhan016/Student-Management-API/actions/workflows/tests.yml/badge.svg)](https://github.com/kirubanandhan016/Student-Management-API/actions/workflows/tests.yml)

A beginner-friendly REST API built with **Python and FastAPI** for retrieving student records, filtering by department, and calculating academic summaries.

This is an introductory API project. It uses sample records stored in memory and does not currently provide persistent database storage or create/update/delete endpoints.

## Features

- List all sample student records
- Retrieve an individual student by ID
- Filter records by department (case-insensitive)
- Search for students meeting a marks threshold
- Calculate student count and average marks
- Return HTTP 404 when a student ID is not found
- Validate query parameters and return HTTP 422 for invalid values
- Interactive OpenAPI documentation through Swagger UI and ReDoc
- Automated endpoint tests with pytest

## Technology

Python 3.11+ · FastAPI · Uvicorn · Pytest · HTTPX

## Project structure

```text
Student-Management-API/
├── .github/
│   └── workflows/
│       └── tests.yml
├── tests/
│   └── test_main.py
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## Run locally

Clone the repository:

```bash
git clone https://github.com/kirubanandhan016/Student-Management-API.git
cd Student-Management-API
```

Create and activate a virtual environment:

**Windows PowerShell**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies and start the server:

```bash
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

The API is available at `http://127.0.0.1:8000`.

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/students` | List all students and return the count |
| GET | `/students/{student_id}` | Retrieve one student by ID |
| GET | `/filter-students?department=ECE` | Filter by department |
| GET | `/students/search/by-marks?min_marks=80` | Find students at or above a marks threshold |
| GET | `/summary` | Return total students and average marks |

The `min_marks` query parameter must be between 0 and 100. It defaults to 80. The `department` parameter must contain 1–50 characters.

## Interactive API documentation

When the server is running:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- OpenAPI schema: `http://127.0.0.1:8000/openapi.json`

## Run tests

```bash
python -m pytest -v
```

GitHub Actions runs the same test suite on pushes and pull requests. Tests cover listing, lookup, 404 handling, department filtering, marks threshold validation, and empty-dataset summary behavior.

## Concepts demonstrated

- FastAPI route declarations and REST-style GET endpoints
- Path and query parameters
- HTTP status codes and exception handling
- Filtering and aggregation with Python lists
- Query validation
- Automated API tests and CI

## Current limitations and next steps

- Data is stored in a Python list and resets when the process restarts.
- There is no SQLAlchemy model or database integration yet.
- Create, update, and delete endpoints are not implemented.
- Authentication and authorization are outside this project's current scope.

A useful next iteration would introduce Pydantic response models, SQLAlchemy 2.0, PostgreSQL persistence, Alembic migrations, and CRUD endpoints. The larger [InventoryX API](https://github.com/kirubanandhan016/inventoryx-fastapi) and [Job Portal API](https://github.com/kirubanandhan016/job-portal-api) demonstrate more advanced backend features.

## Author

**Kirubanandhan V** · [GitHub](https://github.com/kirubanandhan016) · [Portfolio](https://kirubanandhan016.github.io/) · [LinkedIn](https://www.linkedin.com/in/kirubanandhan-v-98bb83443/) · [Email](mailto:kirubanandhan016@gmail.com)
