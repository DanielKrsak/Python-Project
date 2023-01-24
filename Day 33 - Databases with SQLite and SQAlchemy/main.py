from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


@app.route('/')
def home():
    all_books = Books.query.all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = Books(title=request.form["name"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(book)
        db.session.commit()
        return redirect("/")
    return render_template("add.html")


@app.route("/edit/<book_id>", methods=["GET", "POST"])
def edit_rating(book_id):
    selected_book = Books.query.filter_by(id=book_id).first()
    if request.method == "POST":
        selected_book.rating = request.form["new_rating"]
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", id=book_id, book=selected_book)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = Books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

