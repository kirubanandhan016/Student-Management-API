# 🎓 Student Management API

A beginner-friendly REST API built with **Python and FastAPI** to retrieve student records, filter students by department, and calculate academic statistics.

This project demonstrates core backend development concepts, including API endpoints, path parameters, query parameters, JSON responses, HTTP status codes, and error handling.

## 🚀 Features

- 📋 **View All Students** — Retrieve all student records.
- 🔍 **Get Student by ID** — Fetch an individual student's details.
- 🏫 **Filter by Department** — Find students belonging to a particular department.
- 📊 **Academic Summary** — Calculate the total number of students and average marks.
- ⚠️ **Error Handling** — Return a `404 Not Found` response when a student ID does not exist.
- 📖 **Interactive API Documentation** — Test endpoints using Swagger UI.
- 🐍 **Python Type Hints** — Use typed path parameters for automatic validation.

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Server:** Uvicorn
- **API Format:** REST / JSON
- **Documentation:** Swagger UI and ReDoc
- **Development Environment:** Visual Studio Code

## 📁 Project Structure

```text
student_api/
├── main.py
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/kirubanandhan016/Student-Management-API.git
cd Student-Management-API
```

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install "fastapi[standard]"
```

### 4. Run the application

```bash
fastapi dev main.py
```

The API will be available at:

`http://127.0.0.1:8000`

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| GET | `/students` | Retrieve all students |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| GET | `/filter-students?department=ECE` | Filter students by department |
| GET | `/summary` | Get student count and average marks |

## 🧪 Example API Requests

### 1. Retrieve all students

```http
GET /students
```

Example response:

```json
{
  "count": 3,
  "students": [
    {
      "id": 1,
      "name": "Arun",
      "department": "ECE",
      "marks": 85
    },
    {
      "id": 2,
      "name": "Priya",
      "department": "CSE",
      "marks": 92
    },
    {
      "id": 3,
      "name": "Kumar",
      "department": "ECE",
      "marks": 78
    }
  ]
}
```

### 2. Retrieve a student by ID

```http
GET /students/1
```

Example response:

```json
{
  "id": 1,
  "name": "Arun",
  "department": "ECE",
  "marks": 85
}
```

If the student does not exist, the API returns a `404 Not Found` response.

### 3. Filter students by department

```http
GET /filter-students?department=ECE
```

Returns students belonging to the ECE department.

### 4. View the academic summary

```http
GET /summary
```

Example response:

```json
{
  "total_students": 3,
  "average_marks": 85.0
}
```

## 📖 Interactive Documentation

After starting the server, open:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

Use these interfaces to inspect and test your API endpoints.

## 🧠 Concepts Learned

- FastAPI application setup
- REST API fundamentals
- HTTP GET requests
- Path and query parameters
- Python lists and dictionaries
- Loops and conditional statements
- JSON responses
- HTTP exceptions and status codes
- Automatic request validation
- API documentation

## 🔮 Future Enhancements

- Add student creation using POST.
- Implement student updates using PUT and PATCH.
- Implement student deletion using DELETE.
- Integrate an SQLite database for persistent storage.
- Add Pydantic request and response models.
- Write automated tests using Pytest.
- Add pagination and search functionality.

## 👨‍💻 Author

**Kirubanandhan V**

Electronics and Communication Engineering Graduate | Aspiring Python Backend Developer

- GitHub: https://github.com/kirubanandhan016
- LinkedIn: https://www.linkedin.com/in/kirubanandhan-v-98bb83443/

## 📄 License

This project is intended for educational and learning purposes. You may add an MIT License if you want to distribute it as an open-source project.
