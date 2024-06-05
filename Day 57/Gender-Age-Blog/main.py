from flask import Flask, render_template
import random
import datetime
import requests

GENDERIZE_API_URL = "https://api.genderize.io?"
AGIFY_API_URL = "https://api.agify.io?"
BLOG_API_URL = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)


@app.route("/")
def home():
    random_num = random.randint(0, 10)
    today = datetime.date.today()
    year = today.strftime("%Y")
    name = "Lokesh Kumar"
    return render_template(
        "index.html", num=random_num, current_year=year, owner_name=name
    )


@app.route("/guess/<name>")
def guess(name):
    name = name.title()
    genderize_response = requests.get(url=GENDERIZE_API_URL, params={"name": name})
    agify_response = requests.get(url=AGIFY_API_URL, params={"name": name})
    gender = genderize_response.json()["gender"]
    age = agify_response.json()["age"]

    return render_template("guess_name.html", name=name, age=age, gender=gender)


@app.route("/blog")
def get_blog():
    blog_response = requests.get(url=BLOG_API_URL)
    all_posts = blog_response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
