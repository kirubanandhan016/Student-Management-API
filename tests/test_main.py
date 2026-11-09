from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from main import app, students


@pytest.fixture
def client():
    original_students = deepcopy(students)
    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        students[:] = original_students


def test_list_students_returns_count_and_records(client):
    response = client.get("/students")

    assert response.status_code == 200
    assert response.json()["count"] == 3
    assert len(response.json()["students"]) == 3


def test_get_student_returns_record_or_404(client):
    found = client.get("/students/1")
    missing = client.get("/students/999")

    assert found.status_code == 200
    assert found.json()["name"] == "Arun"
    assert missing.status_code == 404


def test_department_filter_is_case_insensitive(client):
    response = client.get("/filter-students", params={"department": "ece"})

    assert response.status_code == 200
    assert response.json()["count"] == 2
    assert all(item["department"] == "ECE" for item in response.json()["students"])


def test_marks_search_uses_default_threshold(client):
    response = client.get("/students/search/by-marks")

    assert response.status_code == 200
    assert response.json()["minimum_marks"] == 80
    assert [student["name"] for student in response.json()["students"]] == ["Arun", "Priya"]


@pytest.mark.parametrize("min_marks", [-1, 101])
def test_marks_search_rejects_out_of_range_threshold(client, min_marks):
    response = client.get(
        "/students/search/by-marks",
        params={"min_marks": min_marks},
    )

    assert response.status_code == 422


def test_summary_returns_average_and_handles_empty_dataset(client):
    response = client.get("/summary")
    assert response.status_code == 200
    assert response.json() == {"total_students": 3, "average_marks": 85.0}

    students.clear()
    empty_response = client.get("/summary")
    assert empty_response.status_code == 200
    assert empty_response.json() == {"total_students": 0, "average_marks": 0.0}
