# The purpose of this project is to allow a easy dashboard like functions to occur on a webpage

from flask import Flask, render_template, jsonify, request, session, flash, url_for


# allows the ability to create webpages
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run()