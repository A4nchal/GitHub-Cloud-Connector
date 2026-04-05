# GitHub Cloud Connector

A backend service built using **FastAPI** that integrates with the **GitHub REST API** to perform core actions like fetching repositories, listing issues, and creating issues.

---

## Objective

This project demonstrates:

* Integration with external APIs (GitHub)
* Secure authentication using Personal Access Token (PAT)
* Clean and modular backend architecture
* REST API design with proper request/response validation

---

## 🛠️ Tech Stack

* **Backend:** Python
* **Framework:** FastAPI
* **HTTP Client:** requests
* **Validation:** Pydantic

---

## 🔐 Authentication

This project uses **GitHub Personal Access Token (PAT)** for authentication.

* Token is stored securely in a `.env` file
* No hardcoding of sensitive credentials

---

## 📁 Project Structure

```
github-connector/
│── app/
│   ├── main.py
│   ├── routes/
│   │   └── github_routes.py
│   ├── services/
│   │   └── github_service.py
│   ├── config/
│   │   └── settings.py
│   └── models/
│       └── schemas.py
│
│── .env
│── requirements.txt
│── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-link>
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add Environment Variables

Create a `.env` file in root:

```
GITHUB_TOKEN=your_personal_access_token
```

Generate token from GitHub → Settings → Developer Settings → Personal Access Tokens → Fine-grained tokens

Here, you need to give permission to access the metadata and issues for the repository:
 
1. Repository Access : Only select repositories → Choose any repository
2. Repository permissions : For Metadata → Read-only
                            For Issues → Read and Write
---

### 5. Run the Application

```bash
uvicorn app.main:app --reload
or
python -m uvicorn app.main:app --reload
```

---

## 🌐 API Documentation

Once the server is running, open:

👉 http://127.0.0.1:8000/docs

Interactive Swagger UI will be available for testing APIs.

---

## 📡 API Endpoints

### 🔹 1. Fetch Repositories

**GET** `/repos/{username}`

Returns list of public repositories for a user.

---

### 🔹 2. List Issues

**GET** `/issues/{owner}/{repo}`

Returns all issues for a repository.

---

### 🔹 3. Create Issue

**POST** `/create-issue`

Creates a new issue in a repository.

#### Request Body:

```json
{
  "owner": "your-username",
  "repo": "your-repo",
  "title": "Test Issue",
  "body": "Created via API"
}
```

---

## ✅ Features

* Secure authentication using environment variables
* Clean separation of concerns (routes, services, config)
* Pydantic schemas for request/response validation
* Error handling for API failures
* Swagger-based interactive API testing

---

## 🧪 Testing

### Using Swagger UI

* Open `/docs`
* Test all endpoints interactively

### Test Cases Covered

* Valid and invalid usernames
* Non-existing repositories
* Unauthorized access (invalid token)
* Issue creation verification on GitHub

---

## ⚠️ Error Handling

Handled scenarios:

* Invalid GitHub token (401 Unauthorized)
* Repository not found (404)
* Invalid input (422 Validation Error)
* GitHub API failures

---

## 👩‍💻 Author

**Aanchal Maheshwari**

---
