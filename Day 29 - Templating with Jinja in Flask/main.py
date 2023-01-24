from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route('/')
def home():
    return render_template("index.html", blogs=blog_response)


@app.route("/post/<blog_id>")
def blog(blog_id):
    return render_template("post.html", id=int(blog_id), blogs=blog_response)


if __name__ == "__main__":
    app.run(debug=True)
