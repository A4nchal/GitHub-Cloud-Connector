from pydantic import BaseModel, Field
from typing import Optional, List


# ----------- REQUEST MODELS -----------

class CreateIssueRequest(BaseModel):
    owner: str = Field(..., example="octocat")
    repo: str = Field(..., example="Hello-World")
    title: str = Field(..., example="Bug found")
    body: Optional[str] = Field(None, example="There is a bug in API")


# ----------- RESPONSE MODELS -----------

class RepoResponse(BaseModel):
    id: int
    name: str
    full_name: str
    private: bool


class IssueResponse(BaseModel):
    id: int
    title: str
    state: str
    html_url: str


# ----------- LIST WRAPPERS -----------

class RepoListResponse(BaseModel):
    repos: List[RepoResponse]


class IssueListResponse(BaseModel):
    issues: List[IssueResponse]