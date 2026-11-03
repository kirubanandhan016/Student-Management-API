# Student Management API

A beginner-friendly REST API built with Python and FastAPI. It serves a small in-memory student dataset and demonstrates path parameters, query parameters, JSON responses, HTTP status codes, and automatic API documentation.

## Implemented functionality

- Retrieve all students
- Retrieve a student by ID
- Filter students by department
- Search students whose marks meet a minimum threshold
- Calculate the student count and average marks
- Return HTTP 404 when a requested student ID does not exist

**Scope:** The current implementation is read-only. It does not yet provide student creation, update, or deletion endpoints, and it does not use a database. The sample data is defined in `main.py`.

## Technology

Python 3 · FastAPI · Uvicorn · Pydantic validation · JSON · Swagger UI / ReDoc

## Project structure

```text
Student-Management-API/
├── main.py
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/kirubanandhan016/Student-Management-API.git
cd Student-Management-API
```

Create and activate a virtual environment:

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install FastAPI with its standard development tools:

```bash
python -m pip install "fastapi[standard]"
```

## Run the API

```bash
fastapi dev main.py
```

Base URL: `http://127.0.0.1:8000`

Interactive documentation:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/students` | Retrieve all students and the result count |
| GET | `/students/{student_id}` | Retrieve one student by ID |
| GET | `/filter-students?department=ECE` | Filter students by department |
| GET | `/students/search/by-marks?min_marks=80` | Find students at or above the minimum marks (default: 80) |
| GET | `/summary` | Return total students and average marks |

There is no `GET /` status route in the current source. Use the generated OpenAPI documentation to inspect the running application.

## Example requests

Retrieve all students:

```http
GET /students
```

Filter by department:

```http
GET /filter-students?department=ECE
```

Search by marks:

```http
GET /students/search/by-marks?min_marks=80
```

Get the academic summary:

```http
GET /summary
```

The API returns JSON. Student records currently contain `id`, `name`, `department`, and `marks`.

## Error handling

A student ID that does not exist returns `404 Not Found`. FastAPI validates the integer path parameter and query parameter types automatically.

## Tests

An automated test suite is not currently present in this repository. Add Pytest and FastAPI TestClient tests before describing the API as fully tested.

## Future improvements

- Add POST, PUT/PATCH, and DELETE endpoints.
- Introduce Pydantic request and response models.
- Persist student records with SQLAlchemy and SQLite/PostgreSQL.
- Add pagination and more filtering.
- Add Pytest coverage for successful requests, invalid inputs, and missing records.

## Author

**Kirubanandhan V**

- GitHub: [@kirubanandhan016](https://github.com/kirubanandhan016)
- LinkedIn: [Kirubanandhan V](https://www.linkedin.com/in/kirubanandhan-v-98bb83443/)
