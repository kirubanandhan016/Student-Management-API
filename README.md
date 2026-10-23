🎓 Student Management API

A simple and efficient REST API built with FastAPI to manage student records, filter students by department, search by marks, and generate student performance summaries.

✨ Features
📋 Retrieve all student records
🔍 Find a student by ID
🏫 Filter students by department
📊 Search students by minimum marks
📈 View total students and average marks
⚡ Fast and interactive API documentation with Swagger UI
🛠️ Tech Stack
Language: Python
Framework: FastAPI
Server: Uvicorn
📁 Project Structure
Student-Management-API/
├── main.py
├── README.md
└── requirements.txt

🚀 Getting Started
1. Clone the repository
git clone https://github.com/kirubanandhan016/Student-Management-API.git
cd Student-Management-API

2. Install dependencies
pip install fastapi uvicorn

3. Run the application
uvicorn main:app --reload

4. Explore the API

Once the server is running, open:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
📡 API Endpoints
Method	Endpoint	Description
GET	/students	Retrieve all students
GET	/students/{student_id}	Retrieve a student by ID
GET	/filter-students?department=ECE	Filter by department
GET	/students/search/by-marks?min_marks=80	Search by minimum marks
GET	/summary	Get student statistics
💡 Example Response

GET /students

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

📊 Student Summary

The /summary endpoint provides:

Total number of students
Average marks across all students
🔮 Future Improvements
Add, update, and delete student records
Integrate a database such as MySQL or PostgreSQL
Implement input validation and error handling
Add authentication and authorization
👨‍💻 Author

Kirubanandhan

GitHub: @kirubanandhan016

⭐ If you find this project useful, consider giving it a star!

Built with Python and FastAPI.
