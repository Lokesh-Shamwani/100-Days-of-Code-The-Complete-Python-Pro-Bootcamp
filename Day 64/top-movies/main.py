from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float, URL
import requests
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()


TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
TMDB_MOVIE_DETAILS_URL = "https://api.themoviedb.org/3/movie"
TMBD_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
TMDB_API_KEY = os.getenv('TMDB_API_KEY')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {BEARER_TOKEN}",
}

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
Bootstrap4(app)

db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


class AddMovieForm(FlaskForm):
    movie_title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


class EditForm(FlaskForm):
    rating = StringField(
        label="Your Rating out of 10 e.g. 7.5", validators=[DataRequired()]
    )
    review = StringField(
        label="Your Review",
        validators=[DataRequired()],
    )
    submit = SubmitField(label="Done")


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    movies = result.scalars().all()

    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()

    return render_template("index.html", all_movies=movies, no_of_movies=len(movies))


@app.route("/edit", methods=["GET", "POST"])
def edit_rating_and_review():
    edit_form = EditForm()
    movie_id = request.args.get("id")
    movie_to_update = db.get_or_404(Movie, movie_id)

    if request.method != "GET":
        if edit_form.validate_on_submit():
            new_rating = edit_form.rating.data
            new_review = edit_form.review.data
            movie_to_update.rating = new_rating
            movie_to_update.review = new_review
            db.session.commit()
            return redirect(url_for("home"))
    else:
        return render_template("edit.html", form=edit_form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    add_movie_form = AddMovieForm()
    if request.method == "POST":
        desired_movie = add_movie_form.movie_title.data
        parameters = {
            "api_key": TMDB_API_KEY,
            "query": desired_movie,  # Pass 'desired_movie' as a query parameter
        }
        response = requests.get(TMDB_SEARCH_URL, parameters)
        search_results = response.json()["results"]
        movies_data = {}

        for element in search_results:
            movies_data[f"{element['original_title']}"] = {
                "tmdb_id": f"{element['id']}",
                "release_date": f"{element['release_date']}",
            }

        return render_template("select.html", all_movies=movies_data)

    else:
        return render_template("add.html", form=add_movie_form)


@app.route("/fetch_movie_details")
def fetch_movie_data():
    movie_id = request.args.get("movie_id")
    response = requests.get(
        f"{TMDB_MOVIE_DETAILS_URL}/{movie_id}", params={"api_key": TMDB_API_KEY}
    )

    data = response.json()

    movie_title = data["original_title"]
    image_url = f"{TMBD_IMAGE_URL}{data['poster_path']}"
    year = data["release_date"].split("-")[0]
    description = data["overview"]

    new_movie = Movie(
        title=movie_title, img_url=image_url, year=year, description=description
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit_rating_and_review", id=new_movie.id))


if __name__ == "__main__":
    app.run(debug=True)
