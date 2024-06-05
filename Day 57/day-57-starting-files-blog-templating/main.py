from flask import Flask, render_template
from post import Post
import requests

BLOG_API_URL = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)

blog_response = requests.get(url=BLOG_API_URL)
all_posts = blog_response.json()
post_objects = []
for post in all_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)


@app.route(rule="/posts/<int:postid>")
def get_post(postid):
    for post in post_objects:
        if postid == post.id:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
