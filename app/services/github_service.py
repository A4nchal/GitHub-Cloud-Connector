import requests
from app.config.settings import settings

BASE_URL = "https://api.github.com"

headers = {
    "Authorization": f"token {settings.github_token}",
    "Accept": "application/vnd.github+json"
}

def get_user_repos(username: str):
    url = f"{BASE_URL}/users/{username}/repos"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.json()}")

    return response.json()


def create_issue(owner: str, repo: str, title: str, body: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"

    payload = {
        "title": title,
        "body": body
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 201:
        raise Exception(f"GitHub API error: {response.json()}")

    return response.json()


def list_issues(owner: str, repo: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.json()}")

    return response.json()