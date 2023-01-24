from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError
import requests


app = Flask(__name__)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_email = User.query.filter_by(email=request.form.get("email")).first()
        hashed_password = generate_password_hash(request.form.get("password"), method="pbkdf2:sha256", salt_length=10)
        new_user = User(
            email=request.form.get("email"),  # type: ignore
            name=request.form.get("name"),  # type: ignore
            password=hashed_password  # type: ignore
        )
        try:
            login_user(new_user)
            db.session.add(new_user)
            db.session.commit()
            logged_in = True
            return render_template("secrets.html", logged_in=logged_in, name=new_user.name)
        except IntegrityError:
            flash("This email already exists. Try logging in instead.")

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form.get("email")).first()
        if user:
            if check_password_hash(user.password, request.form.get("password")):
                login_user(user)
                logged_in = True
                return render_template("secrets.html", logged_in=logged_in, name=user.name)
            else:
                flash("Password does not match your email account. Try again!")
                return redirect(url_for("login"))
        else:
            flash("This email does not exist. Try again or sign up!")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))



@app.route('/download')
def download():
    return send_from_directory(directory='static/files', path="cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
