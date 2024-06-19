from flask import Flask, render_template, request
import requests
from post import Post
from smtplib import SMTP
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

# USE YOUR OWN npoint LINK! 
posts = requests.get(f"https://api.npoint.io/{os.getenv('API_KEY')}").json()
posts_objects = []

for post in posts:
    obj = Post(
        post_id=post["id"],
        title=post["title"],
        subtitle=post["subtitle"],
        body=post["body"],
    )
    posts_objects.append(obj)

app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts_objects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    message_status = False
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:NEW MESSAGE\n\nName:{name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}",
            )
            message_status = True

        print(name, phone, email, message)
        return render_template("contact.html", message_sent=message_status)

    else:
        return render_template("contact.html", message_sent=message_status)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(
        debug=True,
    )
