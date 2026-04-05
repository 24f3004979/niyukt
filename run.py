from flask import Flask, render_template
from api.registration import register
from api.admin import admin
from api.company import company

app = Flask(__name__)

app.secret_key = "Ironman"

app.register_blueprint(register)
app.register_blueprint(admin)
app.register_blueprint(company)

@app.route("/")
def launch():
    return render_template('index.html')
# BUG : Anyone can access admin any one can access the other account

if __name__ == "__main__":
    app.run(debug=True, port=8080)

