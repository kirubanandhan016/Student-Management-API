from fastapi import FastAPI, HTTPException, Query

app = FastAPI(
    title="Student Management API",
    description="A beginner project for retrieving and analyzing student records.",
    version="1.1.0",
)

# Sample data is intentionally held in memory for this introductory project.
students = [
    {"id": 1, "name": "Arun", "department": "ECE", "marks": 85},
    {"id": 2, "name": "Priya", "department": "CSE", "marks": 92},
    {"id": 3, "name": "Kumar", "department": "ECE", "marks": 78},
]


@app.get("/students", summary="List all students")
def get_students():
    return {"count": len(students), "students": students}


@app.get("/students/{student_id}", summary="Get a student by ID")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


@app.get("/filter-students", summary="Filter students by department")
def filter_students(department: str = Query(min_length=1, max_length=50)):
    result = [
        student
        for student in students
        if student["department"].lower() == department.strip().lower()
    ]
    return {
        "department": department,
        "count": len(result),
        "students": result,
    }


@app.get("/students/search/by-marks", summary="Find students meeting a marks threshold")
def search_by_marks(
    min_marks: int = Query(default=80, ge=0, le=100),
):
    result = [student for student in students if student["marks"] >= min_marks]
    return {
        "minimum_marks": min_marks,
        "count": len(result),
        "students": result,
    }


@app.get("/summary", summary="Calculate student performance summary")
def get_summary():
    if not students:
        return {"total_students": 0, "average_marks": 0.0}

    total_marks = sum(student["marks"] for student in students)
    average = total_marks / len(students)
    return {
        "total_students": len(students),
        "average_marks": round(average, 2),
    }
