from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello, it's FastAPI"}
