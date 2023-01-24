from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

API_KEY = "1502ddb7684113d6bb1fef1d0b3292ed"
SEARCH_ENDPOINT = "https://api.themoviedb.org/3/search/movie"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Movie.db"
db = SQLAlchemy(app)
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String, nullable=True)


# db.create_all()


class MyForm(FlaskForm):
    rating = FloatField('Your Rating out of 10', validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Submit")


class AddForm(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    # db.session.add(new_movie)
    # db.session.commit()
    movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        movies[i].ranking = len(movies) - i
    return render_template("index.html", movies=movies)


@app.route("/update/<int:id>", methods=["POST", "GET"])
def update(id):
    form = MyForm()
    movie = Movie.query.get(id)
    if form.validate_on_submit():
        movie.rating = request.form.get("rating")
        movie.review = request.form.get("review")
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", form=form, movie=movie)


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    movie = Movie.query.get(id)
    try:
        db.session.delete(movie)
        db.session.commit()
        return redirect("/")
    except:
        return "Something went wrong. Try again!"


@app.route("/add", methods=["POST", "GET"])
def add_movie():
    form = AddForm()
    if form.validate_on_submit():
        searched_movie = form.data.get("movie_title")
        search_params = {
            "query": searched_movie,
            "api_key": API_KEY
        }
        movie_response = requests.get(SEARCH_ENDPOINT, params=search_params).json()["results"]
        return render_template("select.html", movies=movie_response)
    return render_template("add.html", form=form)


@app.route("/find/<int:id>")
def find_movie(id):
    find_params = {
        "api_key": API_KEY
    }
    find_response = requests.get(f"https://api.themoviedb.org/3/movie/{id}", params=find_params).json()
    new_movie = Movie(
            title=find_response["belongs_to_collection"]["name"],
            year=find_response["release_date"],
            description=find_response["overview"],
            rating=0,
            ranking=0,
            review="",
            img_url=f"https://image.tmdb.org/t/p/w500{find_response['backdrop_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("update", id=new_movie.id))



if __name__ == '__main__':
    app.run(debug=True)
