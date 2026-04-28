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
