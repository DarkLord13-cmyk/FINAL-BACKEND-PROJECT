# Task Manager Django Backend

A complete Django REST Framework application for managing tasks and projects, complete with Swagger UI documentation and custom data visualization endpoints.

## Features
- **Projects**: Create, Read, Update, Delete projects.
- **Tasks**: Create, Read, Update, Delete tasks.
- **Data Visualization API**: Endpoint to fetch task counts grouped by status.
- **API Documentation**: Built-in Swagger UI and ReDoc using `drf-yasg`.

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd django_task_manager
```

### 2. Set up virtual environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables
Copy the example environment file and fill in your values.
```bash
cp .env.example .env
```

### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Server
```bash
python manage.py runserver
```

## API Documentation

Once the server is running, you can access the API documentation at:
- Swagger UI: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`

## How to push to GitHub

To push this repository to your own GitHub account:

1. Go to GitHub and create a new empty repository (do not initialize it with a README, .gitignore, or license).
2. Open your terminal in the project directory.
3. Run the following commands:
```bash
git remote add origin https://github.com/your-username/your-repo-name.git
git branch -M main
git push -u origin main
```
