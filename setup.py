from setuptools import setup, find_packages

setup(
    name="fastapi-crud-app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # FastAPI and related packages
        "fastapi>=0.109.2",
        "uvicorn>=0.27.1",
        "pydantic>=2.5.2",
        "pydantic-settings>=2.1.0",
        "python-multipart>=0.0.9",
        "email-validator>=2.1.0.post1",

        # Database support
        "sqlalchemy>=2.0.29",
        "psycopg2-binary>=2.9.9",

        # Authentication
        "python-jose>=3.3.0",
        "passlib>=1.7.4",

        # Web server
        "gunicorn>=23.0.0",

        # Flask (support for Flask patterns and utils)
        "flask>=2.3.3",
        "flask-sqlalchemy>=3.1.1",
    ],
    python_requires=">=3.9",
)