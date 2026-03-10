from flask import Flask, render_template
from api.registration import register
from api.adminv2 import admin

app = Flask(__name__)

app.secret_key = "Ironman"

app.register_blueprint(register)
app.register_blueprint(admin)

@app.route("/")
def launch():
    return '<h1> Landing Page </h1>'


if __name__ == "__main__":
    app.run(debug=True, port=8080)

