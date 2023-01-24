from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

rating_choice = ["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"]
wifi_choice = ["💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
socket_choice = ["🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"]


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps', validators=[DataRequired()])
    open = StringField('Opening Time', validators=[DataRequired()])
    close = StringField('Closing Time', validators=[DataRequired()])
    rating = SelectField('Coffee Rating', choices=rating_choice , validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating', choices=wifi_choice, validators=[DataRequired()])
    socket = SelectField('Power Socket Availability', choices=socket_choice, validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        data = [form.cafe.data, form.location.data,
                form.open.data, form.close.data,
                form.rating.data, form.wifi.data, form.socket.data]
        with open("cafe-data.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow(data)
        return redirect("/cafes")
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

