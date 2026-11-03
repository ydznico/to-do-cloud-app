# Cloud-Native To-Do List Manager

A beginner-friendly task manager built with Python Flask. It demonstrates the application side of an end-to-end cloud-native deployment assignment using Docker, Amazon ECR, Amazon EKS, GitHub Actions, and Argo CD.

## Features

- Add tasks
- Mark tasks as completed or pending
- Delete tasks
- View pending and completed task counts
- Automated tests with pytest

## Project structure

```text
todo-cloud-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── tests/
    └── test_app.py
```

## Run locally

Python 3.10 or newer is recommended.

### Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000.

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000.

## Run tests

With the virtual environment activated:

```bash
python -m pytest -v
```

## Build and run with Docker

```bash
docker build -t todo-cloud-app:v1 .
docker run --rm -p 5000:5000 todo-cloud-app:v1
```

Open http://localhost:5000.

## Important note about data

This starter version stores tasks in application memory to keep the assignment simple. Tasks are reset when the application process restarts, and separate replicas do not share task data. This is suitable for demonstrating the deployment pipeline, but a persistent database would be needed for a production multi-replica application.

## Cloud deployment stages

The remaining assignment stages are to:

1. Push the source code to GitHub.
2. Build and publish the Docker image to Amazon ECR.
3. Deploy the image to Amazon EKS using Kubernetes manifests.
4. Configure GitHub Actions to test, build, and push images using GitHub OIDC with AWS IAM.
5. Configure Argo CD to synchronize Kubernetes manifests from Git.

These cloud resources and workflows are not created by this starter project; they will be configured during the deployment steps.
