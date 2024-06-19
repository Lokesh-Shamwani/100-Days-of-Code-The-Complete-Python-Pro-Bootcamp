from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
Bootstrap5(app)
ckeditor = CKEditor(app)

# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


class PostForm(FlaskForm):
    title = StringField("Blog Post Title")
    subtitle = StringField("Subtitle")
    author = StringField("Your Name")
    img_url = StringField("Blog Image URL")
    content = CKEditorField("Blog Content")
    submit = SubmitField("Submit Post")


with app.app_context():
    db.create_all()


@app.route("/")
def get_all_posts():
    result = db.session.execute(db.select(BlogPost).order_by(BlogPost.title))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = db.session.execute(
        db.select(BlogPost).where(BlogPost.id == post_id)
    ).scalar()
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    blog_post_form = PostForm()
    if request.method == "POST":
        title = request.form.get("title")
        subtitle = request.form.get("subtitle")
        author = request.form.get("author")
        img_url = request.form.get("img_url")
        body = request.form.get("content")
        now = datetime.now()
        date = f"{now.strftime('%B')} {now.strftime('%d')}, {now.strftime('%Y')}"
        new_blog_post = BlogPost(
            title=title,
            subtitle=subtitle,
            author=author,
            img_url=img_url,
            body=body,
            date=date,
        )
        db.session.add(new_blog_post)
        db.session.commit()

        return redirect(url_for("get_all_posts"))
    else:
        return render_template("make-post.html", form=blog_post_form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = PostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        content=post.body
    )
    if request.method == "POST":
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.author = edit_form.author.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.content.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    else:
        return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
