from flask import Flask, render_template
from API.registration import register
from model.student import *

app = Flask(__name__)

app.register_blueprint(register)

@app.route("/")
def launch():
    return '<h1> Landing Page </h1>'




if __name__ == "__main__":
    app.run(debug=True)

