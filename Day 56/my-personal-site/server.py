from flask import Flask
from flask import render_template

app = Flask(__name__)
print(__name__)


@app.route("/")
def home():
    return render_template("lokesh.html")


if __name__ == "__main__":
    app.run(debug=True)
