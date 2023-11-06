from flask import Flask
from flask import Response

app = Flask(__name__)


@app.route("/")
def root():
    return Response("Hello from Flask")


app = app.wsgi_app
