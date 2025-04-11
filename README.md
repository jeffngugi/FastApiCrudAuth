# FastAPI CRUD Application

A RESTful API built with FastAPI, featuring user authentication and PostgreSQL database integration.

## Features

- User authentication with JWT
- CRUD operations for users and items
- RESTful API design
- PostgreSQL database integration
- Swagger UI documentation

## Requirements

- Python 3.11+
- PostgreSQL database
- Dependencies listed in pyproject.toml

## Environment Variables

The application uses the following environment variables:

```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
PGHOST=localhost
PGPORT=5432
PGUSER=postgres
PGPASSWORD=yourpassword
PGDATABASE=app
SECRET_KEY=yoursecretkey
```

## Setup and Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fastapi-crud-app
```

2. Install dependencies:
```bash
pip install fastapi uvicorn gunicorn pydantic pydantic-settings python-jose passlib[bcrypt] sqlalchemy psycopg2-binary python-multipart email-validator
```

3. Set up the database:
```bash
python -c "from app.database import Base, engine; from app.models import User, Item; Base.metadata.create_all(bind=engine)"
```

## Running the Application

### Method 1: Using Replit Workflow

The application is configured to run in Replit using the "Start application" workflow, which uses Gunicorn.

Note: In the current Gunicorn setup, only the root endpoint is accessible due to WSGI/ASGI compatibility issues.

### Method 2: Using Gunicorn (Production)

```bash
gunicorn --bind 0.0.0.0:5000 --reload main:app
```

### Method 3: Using Uvicorn (Development, Recommended)

For full functionality including all API endpoints and Swagger UI:

```bash
python run_uvicorn.py
```

or directly:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

To run Uvicorn in Replit, you can modify the workflow command to:
```
uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload
```

## API Documentation

When running with Uvicorn, the API documentation is available at:

- Swagger UI: `/docs`
- ReDoc: `/redoc`

## API Endpoints

### Authentication
- `POST /api/v1/users/login/access-token` - Get access token

### Users
- `GET /api/v1/users/me` - Get current user
- `PUT /api/v1/users/me` - Update current user
- `POST /api/v1/users/` - Create user
- `GET /api/v1/users/{user_id}` - Get user by ID
- `GET /api/v1/users/` - Get all users (superusers only)

### Items
- `GET /api/v1/items/` - Get user's items
- `POST /api/v1/items/` - Create item
- `GET /api/v1/items/{id}` - Get item by ID
- `PUT /api/v1/items/{id}` - Update item
- `DELETE /api/v1/items/{id}` - Delete item

## Project Structure

```
.
├── app
│   ├── api
│   │   ├── endpoints
│   │   │   ├── items.py
│   │   │   └── users.py
│   │   ├── api.py
│   │   └── deps.py
│   ├── auth.py
│   ├── config.py
│   ├── crud.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── main.py            # WSGI entry point for Gunicorn
├── run_uvicorn.py     # Script to run with Uvicorn for full functionality
└── README.md
```