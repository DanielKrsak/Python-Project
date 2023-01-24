from flask import Flask
from random import randint

app = Flask(__name__)
random_number = randint(0, 9)


@app.route("/")
def home_page():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src=https://media2.giphy.com/media/l378khQxt68syiWJy/" \
           "giphy.gif?cid=ecf05e47cadw37oecqcj7idsa1i4f7g2olh0eqiix342hgbf&rid=giphy.gif&ct=g>"


@app.route("/<int:number>")
def check_number(number):
    if number > random_number:
        return "<h1 style='color:blue;'>Too High,Try Again!</h1>" \
               "<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"
    elif number < random_number:
        return "<h1 style='color:red;'>Too Low, Try Again!</h1>" \
               "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"
    else:
        return "<h1 style='color:green;'>You Found Me!</h1>" \
               "<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"


if __name__ == "__main__":
    app.run(debug=True)