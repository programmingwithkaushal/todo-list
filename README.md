# Todo Application 📝

![CI/CD Pipeline](https://github.com/programmingwithkaushal/todo-list/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen.svg)
![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)
![Docker Ready](https://img.shields.io/badge/docker-ready-blue.svg)

## Project Overview
A production-quality Python Todo Application built with Flask and SQLite. Designed for high reliability, it follows a modular Clean Architecture with RESTful APIs, high code coverage (>90%), and features a full CI/CD pipeline using GitHub Actions.

## Features
- **CRUD Operations**: Create, Read, Update, and Delete tasks.
- **Task Management**: Mark tasks as completed or pending.
- **Search & Filtering**: Search for tasks by keywords or filter by their completion status.
- **CI/CD Pipeline**: Fully automated testing, linting, formatting, and Docker build pipeline via GitHub Actions.
- **Dockerized**: Contains optimized Dockerfile and docker-compose configurations for seamless deployment.

## Folder Structure
```text
todo-app/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── services.py
│   ├── database.py
│   └── utils.py
├── tests/
│   ├── conftest.py
│   ├── test_routes.py
│   ├── test_services.py
│   └── test_database.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── pytest.ini
├── .flake8
├── .gitignore
├── app.py
└── README.md
```

## Installation

### Virtual Environment (Local Setup)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Running Locally
```bash
python app.py
```

### Running Tests
```bash
pytest --cov=app
```

## Docker Commands
### Build the image
```bash
docker build -t todo-app .
```

### Run the container
```bash
docker run -d -p 5000:5000 todo-app
```

## API Examples
### 1. Create a Todo
```bash
curl -X POST http://127.0.0.1:5000/todos -H "Content-Type: application/json" -d '{"title": "Buy groceries", "description": "Milk, Eggs, Bread"}'
```

### 2. Get all Todos
```bash
curl -X GET http://127.0.0.1:5000/todos
```
