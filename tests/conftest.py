from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from main import app, students


@pytest.fixture
def client():
    original_students = deepcopy(students)
    with TestClient(app) as test_client:
        yield test_client
    students[:] = original_students
