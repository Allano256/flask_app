import os
from flask import Flask 
"""
We first import our class Flask
"""

app = Flask(__name__)
"""
We create an instance of it and storing it in the app variable
"""

@app.route("/")

def index():
    return "Hello World"
"""
We use a decorator @ this is a way of wrapping functions
So wen we trigger the root directory, flask returns the code above.
"""
if __name__ == "__main__":
    """
    the word "__main__" is the name of the  the default module in python, first one we shall run.
    Here we create where we want our app to run, set the IP but also give an alternative if it fails,
    Have the debug setv to true during the development stage buh then change it to false before uploading it
    """
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("port", "5000")),
        debug = True
    )