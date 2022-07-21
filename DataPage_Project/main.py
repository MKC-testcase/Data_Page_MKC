# The purpose of this project is to allow a easy dashboard like functions to occur on a webpage

from flask import Flask

# allows the ability to create webpages
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"


if __name__ == "__main__":
    app.run()