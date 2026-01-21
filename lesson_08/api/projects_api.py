import requests


class ProjectsApi:
    def __init__(self, token: str):
        self.token = token
        self.base_url = "https://yougile.com/api-v2/projects"
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def create_project(self, body: dict):
        return requests.post(
            self.base_url, json=body, headers=self.headers
        )

    def get_project(self, project_id: str):
        return requests.get(
            f"{self.base_url}/{project_id}", headers=self.headers
        )

    def update_project(self, project_id: str, body: dict):
        return requests.put(
            f"{self.base_url}/{project_id}", json=body, headers=self.headers
        )

    def delete_project(self, project_id: str):
        return requests.delete(
            f"{self.base_url}/{project_id}", headers=self.headers
        )
