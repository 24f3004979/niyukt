from flask import Flask, render_template
from api.registrationv2 import register
from config import *

app = Flask(__name__)

app.register_blueprint(register)

@app.route("/")
def launch():
    return '<h1> Landing Page </h1>'




if __name__ == "__main__":
    app.run(debug=True)

