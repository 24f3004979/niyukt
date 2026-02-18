from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def launch():
    return render_template("Student_Registration.html")  # Working to serve html

if __name__ == "__main__":
    app.run(debug=True)
