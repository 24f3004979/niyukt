from flask import Flask, render_template, session, flash
from api.registration import register
from api.admin import admin
from api.login import login_route
from api.dashboard import dashboard_route
from api.company_dashboard import company
from api.student_dashboard import *


app = Flask(__name__)

app.secret_key = "Ironman"

app.register_blueprint(register)
app.register_blueprint(admin)
app.register_blueprint(login_route)
app.register_blueprint(dashboard_route)
app.register_blueprint(company)
app.register_blueprint(student)

@app.route("/")
def launch():
    return render_template('index.html')
# BUG : Anyone can access admin any one can access the other account

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    flash("Loged out :)", "success")
    return redirect('http://127.0.0.1:8080/')

if __name__ == "__main__":
    app.run(debug=True, port=8080)
    session.clear()

