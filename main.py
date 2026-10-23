from fastapi import FastAPI ,status,HTTPException
app=FastAPI(
 title="Student Management API",
 description="A beginner project for managing records",
 version="1.0")

students = [
    {"id": 1, "name": "Arun", "department": "ECE", "marks": 85},
    {"id": 2, "name": "Priya", "department": "CSE", "marks": 92},
    {"id": 3, "name": "Kumar", "department": "ECE", "marks": 78},
]
@app.get("/students")
def get_students():
    return {
        "count":len(students),
        "students": students
    }
@app.get("/students/{student_id}")
def get_student(student_id:int):
    for student in students:
        if student["id"]==student_id:
            return student
    raise HTTPException(
        status_code=404,
        detail="student not found"
    )
@app.get("/filter-students")
def filter_students(department:str):
    result=[]

    for student in students:
        if student["department"].lower()==department.lower():
            result.append(student)

    return {
        "department":department,
        "count":len(result),
        "students":result
    }
@app.get("/students/search/by-marks")
def search_by_marks(min_marks: int = 80):
    result = []

    for student in students:
        if student["marks"] >= min_marks:
            result.append(student)

    return {
        "minimum_marks": min_marks,
        "count": len(result),
        "students": result
    }
@app.get("/summary")
def get_summary():
    total_marks = 0

    for student in students:
        total_marks += student["marks"]

    average = total_marks / len(students)

    return {
        "total_students": len(students),
        "average_marks": round(average, 2)
    }
    
 