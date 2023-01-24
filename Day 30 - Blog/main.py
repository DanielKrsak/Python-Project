from flask import Flask, render_template, request
import requests
from smtplib import SMTP

EMAIL = "krsak.danko@yahoo.com"
PASSWORD = "tdjxbyebqischcpt"

blogs = requests.get("https://api.npoint.io/270dbe4516af0562c19b").json()


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", blogs=blogs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        with SMTP("smtp.mail.yahoo.com") as smtp:
            smtp.starttls()
            smtp.login(user=EMAIL, password=PASSWORD)
            smtp.sendmail(from_addr=EMAIL,
                          to_addrs=EMAIL,
                          msg=f"Subject: Test\n\n"
                              f"Name: {request.form['name']}\n "
                              f"Email: {request.form['email']}\n"
                              f"Phone Number: {request.form['phone']}\n"
                              f"Message: {request.form['message']}")
        return render_template("contact.html", method=request.method)
    else:
        return render_template("contact.html", method=request.method)


@app.route("/®post/<int:blog_id>")
def post(blog_id):
    return render_template("post.html", id=blog_id, blogs=blogs)


if __name__ == "__main__":
    app.run(debug=True)