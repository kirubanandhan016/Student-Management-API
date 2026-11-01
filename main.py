from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

app = FastAPI(
    title="Student Management API",
    description="A small REST API for managing in-memory student records.",
    version="2.0.0",
)


class StudentBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    department: str = Field(min_length=1, max_length=30)
    marks: int = Field(ge=0, le=100)

    @field_validator("name", "department", mode="before")
    @classmethod
    def strip_text_fields(cls, value: object) -> object:
        return value.strip() if isinstance(value, str) else value


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    department: str | None = Field(default=None, min_length=1, max_length=30)
    marks: int | None = Field(default=None, ge=0, le=100)

    @field_validator("name", "department", mode="before")
    @classmethod
    def strip_text_fields(cls, value: object) -> object:
        return value.strip() if isinstance(value, str) else value

    @model_validator(mode="after")
    def validate_update_fields(self) -> "StudentUpdate":
        if not self.model_fields_set:
            raise ValueError("At least one field must be provided")
        for field_name in self.model_fields_set:
            if getattr(self, field_name) is None:
                raise ValueError(f"{field_name} cannot be null")
        return self


class StudentRead(StudentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


students: list[StudentRead] = [
    StudentRead(id=1, name="Arun", department="ECE", marks=85),
    StudentRead(id=2, name="Priya", department="CSE", marks=92),
    StudentRead(id=3, name="Kumar", department="ECE", marks=78),
]


@app.get("/")
def health_check() -> dict[str, str]:
    return {"status": "ok", "message": "Student Management API is running"}


@app.post(
    "/students",
    response_model=StudentRead,
    status_code=status.HTTP_201_CREATED,
)
def create_student(payload: StudentCreate) -> StudentRead:
    new_id = max((student.id for student in students), default=0) + 1
    student = StudentRead(id=new_id, **payload.model_dump())
    students.append(student)
    return student


@app.get("/students")
def get_students(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=200),
) -> dict[str, object]:
    page = students[offset : offset + limit]
    return {"count": len(students), "students": page}


@app.get("/students/search/by-marks")
def search_by_marks(
    min_marks: int = Query(default=80, ge=0, le=100),
) -> dict[str, object]:
    result = [student for student in students if student.marks >= min_marks]
    return {
        "minimum_marks": min_marks,
        "count": len(result),
        "students": result,
    }


@app.get("/students/{student_id}", response_model=StudentRead)
def get_student(student_id: int) -> StudentRead:
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


@app.put("/students/{student_id}", response_model=StudentRead)
def replace_student(student_id: int, payload: StudentCreate) -> StudentRead:
    for index, student in enumerate(students):
        if student.id == student_id:
            updated = StudentRead(id=student_id, **payload.model_dump())
            students[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Student not found")


@app.patch("/students/{student_id}", response_model=StudentRead)
def update_student(student_id: int, payload: StudentUpdate) -> StudentRead:
    for index, student in enumerate(students):
        if student.id == student_id:
            updated_data = student.model_dump()
            updated_data.update(payload.model_dump(exclude_unset=True))
            updated = StudentRead(**updated_data)
            students[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Student not found")


@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int) -> None:
    for index, student in enumerate(students):
        if student.id == student_id:
            students.pop(index)
            return
    raise HTTPException(status_code=404, detail="Student not found")


@app.get("/filter-students")
def filter_students(
    department: str = Query(min_length=1, max_length=30),
) -> dict[str, object]:
    normalized_department = department.strip()
    result = [
        student
        for student in students
        if student.department.casefold() == normalized_department.casefold()
    ]
    return {
        "department": normalized_department,
        "count": len(result),
        "students": result,
    }


@app.get("/summary")
def get_summary() -> dict[str, int | float]:
    total_students = len(students)
    average_marks = (
        sum(student.marks for student in students) / total_students
        if total_students
        else 0.0
    )
    return {
        "total_students": total_students,
        "average_marks": round(average_marks, 2),
    }
