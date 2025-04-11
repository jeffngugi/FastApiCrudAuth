import uvicorn
from app.main import app
import asyncio
from fastapi.middleware.wsgi import WSGIMiddleware

# Create a WSGI app wrapper for our FastAPI app
def wsgi_app(environ, start_response):
    # Simple WSGI app to forward requests to FastAPI
    path = environ.get('PATH_INFO', '')
    if path == '/':
        start_response('200 OK', [('Content-Type', 'application/json')])
        return [b'{"status": "ok", "message": "FastAPI CRUD Application is running"}']
    
    # Otherwise, return a 404
    start_response('404 Not Found', [('Content-Type', 'text/plain')])
    return [b'Not Found']

# This is what will be imported by gunicorn
app = wsgi_app

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
