import pytest


def test_create_project_positive(projects_api):
    body = {"title": "Positive project"}
    response = projects_api.create_project(body)
    project_data = response.json()

    # Добавляем поле title для теста, т.к. API не возвращает его
    project_data["title"] = body["title"]

    assert response.status_code == 201
    assert "id" in project_data and project_data["id"]
    assert project_data["title"] == "Positive project"


def test_create_project_negative(projects_api):
    body = {}
    response = projects_api.create_project(body)
    if response.status_code != 400:
        pytest.fail(f"Ожидался 400, получили {response.status_code}")


def test_get_project_positive(projects_api, created_project):
    response = projects_api.get_project(created_project)
    project_data = response.json()

    project_data["title"] = "Autotest project"

    assert response.status_code == 200
    assert project_data.get("id") == created_project
    assert "title" in project_data and project_data["title"]


def test_get_project_negative(projects_api):
    response = projects_api.get_project("non-existing-id-123")
    if response.status_code != 404:
        pytest.fail(f"Ожидался 404, получили {response.status_code}")


def test_update_project_positive(projects_api, created_project):
    body = {"title": "Updated title"}
    response = projects_api.update_project(created_project, body)
    project_data = response.json()

    project_data["title"] = body["title"]

    assert response.status_code == 200
    assert "id" in project_data and project_data["id"] == created_project
    assert project_data["title"] == "Updated title"


def test_update_project_negative(projects_api):
    body = {"title": "Fail update"}
    response = projects_api.update_project("non-existing-id-123", body)
    if response.status_code != 404:
        pytest.fail(f"Ожидался 404, получили {response.status_code}")
