from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library-project.db"

db = SQLAlchemy()

db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )
    author: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    no_of_books = db.session.query(Book).count()
    return render_template("index.html", all_books=all_books, no_of_books=no_of_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["book_name"]
        author = request.form["book_author"]
        rating = request.form["book_rating"]
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("home"))
    else:
        return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit_rating():
    book_id = request.args.get("id")
    book = db.get_or_404(Book, book_id)
    if request.method == "POST":
        new_rating = request.form["new_rating"]
        book.rating = new_rating
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("edit_rating.html", book=book)


@app.route("/delete")
def delete_book():
    book_id = request.args.get("id")
    book = db.get_or_404(Book, book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
