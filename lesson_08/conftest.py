import pytest
from api.projects_api import ProjectsApi
import os


@pytest.fixture
def projects_api():
    token = os.getenv("YOUGILE_TOKEN")
    api = ProjectsApi(token=token)
    return api


@pytest.fixture
def created_project(projects_api):
    body = {"title": "Autotest project"}
    response = projects_api.create_project(body)
    project_id = response.json()["id"]
    yield project_id

    # Удаляем проект после теста
    delete_response = projects_api.delete_project(project_id)
    if delete_response.status_code != 200:
        print(
            f"Внимание: не удалось удалить проект {project_id}. "
            f"Ответ сервера: {delete_response.text}"
        )
