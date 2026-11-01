def test_list_and_summary_return_seeded_students(client):
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json()["count"] == 3
    assert client.get("/summary").json() == {
        "total_students": 3,
        "average_marks": 85.0,
    }


def test_student_crud_flow(client):
    created = client.post(
        "/students",
        json={"name": "Meena", "department": "ECE", "marks": 88},
    )
    assert created.status_code == 201
    student_id = created.json()["id"]

    fetched = client.get(f"/students/{student_id}")
    assert fetched.status_code == 200
    assert fetched.json()["name"] == "Meena"

    updated = client.patch(
        f"/students/{student_id}",
        json={"marks": 91},
    )
    assert updated.status_code == 200
    assert updated.json()["marks"] == 91

    replaced = client.put(
        f"/students/{student_id}",
        json={"name": "Meena S", "department": "CSE", "marks": 94},
    )
    assert replaced.status_code == 200
    assert replaced.json()["department"] == "CSE"

    deleted = client.delete(f"/students/{student_id}")
    assert deleted.status_code == 204
    assert client.get(f"/students/{student_id}").status_code == 404


def test_validation_and_missing_records(client):
    invalid = client.post(
        "/students",
        json={"name": "Bad Marks", "department": "ECE", "marks": 101},
    )
    assert invalid.status_code == 422
    assert client.get("/students/999").status_code == 404
    assert client.patch("/students/1", json={}).status_code == 422


def test_filters_and_search(client):
    assert client.get("/filter-students", params={"department": "ece"}).json()["count"] == 2
    assert client.get("/students/search/by-marks", params={"min_marks": 90}).json()["count"] == 1
