from fastapi import APIRouter, HTTPException
from typing import List

from app.services.github_service import (
    get_user_repos,
    create_issue,
    list_issues
)

from app.models.schemas import (
    RepoResponse,
    IssueResponse,
    CreateIssueRequest
)

router = APIRouter()


# ✅ Fetch Repositories
@router.get("/repos/{username}", response_model=List[RepoResponse])
def fetch_repos(username: str):
    try:
        repos = get_user_repos(username)

        # Filter only required fields
        return [
            {
                "id": repo["id"],
                "name": repo["name"],
                "full_name": repo["full_name"],
                "private": repo["private"]
            }
            for repo in repos
        ]

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ✅ List Issues
@router.get("/issues/{owner}/{repo}", response_model=List[IssueResponse])
def get_issues(owner: str, repo: str):
    try:
        issues = list_issues(owner, repo)

        return [
            {
                "id": issue["id"],
                "title": issue["title"],
                "state": issue["state"],
                "html_url": issue["html_url"]
            }
            for issue in issues
        ]

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ✅ Create Issue
@router.post("/create-issue", response_model=IssueResponse)
def create_new_issue(request: CreateIssueRequest):
    try:
        issue = create_issue(
            request.owner,
            request.repo,
            request.title,
            request.body
        )

        return {
            "id": issue["id"],
            "title": issue["title"],
            "state": issue["state"],
            "html_url": issue["html_url"]
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))