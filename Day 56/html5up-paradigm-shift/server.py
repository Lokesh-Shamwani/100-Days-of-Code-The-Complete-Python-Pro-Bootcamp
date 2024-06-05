from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# document.body.contentEditable=true    #type this in chrome developer tools to change the content in browser, then save it by ctrl+S.

if __name__ == "__main__":
    app.run(debug=True)