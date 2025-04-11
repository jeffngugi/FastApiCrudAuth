import uvicorn
from app.main import app
import asyncio
from fastapi.middleware.wsgi import WSGIMiddleware

# Create a WSGI app wrapper for our FastAPI app
def wsgi_app(environ, start_response):
    # Simple WSGI app to forward requests to FastAPI
    path = environ.get('PATH_INFO', '')
    if path == '/':
        start_response('200 OK', [('Content-Type', 'text/html')])
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>FastAPI CRUD App</title>
            <link href="https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css" rel="stylesheet">
            <style>
                body { padding: 20px; }
                .container { max-width: 800px; margin: 0 auto; }
                .card { margin-bottom: 20px; }
            </style>
        </head>
        <body data-bs-theme="dark">
            <div class="container">
                <div class="card">
                    <div class="card-body">
                        <h1 class="card-title">FastAPI CRUD Application</h1>
                        <div class="alert alert-success">
                            <strong>Status:</strong> The application is running
                        </div>
                        <p class="card-text">This is a RESTful API built with FastAPI, featuring user authentication and PostgreSQL database integration.</p>
                    </div>
                </div>
                
                <div class="card">
                    <div class="card-header">
                        <h3>API Information</h3>
                    </div>
                    <div class="card-body">
                        <p>Note: The Gunicorn setup currently only serves this welcome page.</p>
                        <p>For full API functionality, please run the application using Uvicorn:</p>
                        <pre class="bg-dark text-light p-3 rounded">uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload</pre>
                        
                        <h4 class="mt-4">API Documentation</h4>
                        <p>When running with Uvicorn, API documentation is available at:</p>
                        <ul>
                            <li><a href="/docs" class="disabled">/docs</a> - Swagger UI</li>
                            <li><a href="/redoc" class="disabled">/redoc</a> - ReDoc</li>
                        </ul>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
        return [html.encode('utf-8')]
    
    # Otherwise, return a 404
    start_response('404 Not Found', [('Content-Type', 'text/plain')])
    return [b'Not Found - To access the API, please run using Uvicorn instead of Gunicorn']

# This is what will be imported by gunicorn
app = wsgi_app

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
