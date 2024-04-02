from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from forms import AddCafe
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SECRET_KEY"] = os.environ["SECRETKEY"]
db = SQLAlchemy(app)
bootstrap = Bootstrap5(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/", methods=['POST', 'GET'])
def cafe_names():
    cafes = db.session.execute(db.select(Cafe)).scalars()
    db.session.commit()
    col_names = ["ID", "Names", "Map Url", "Img url", "Location", "Socket Availability", "Toilet Availability",
                 "Wifi Availability", "Can Take Calls?", "Seats", "Price of a Cup'O'Coffee"]
    cafe_list = cafes.all()

    return render_template("home.html", cafes=cafe_list, col_names=col_names)


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = AddCafe()
    if form.validate_on_submit():
        new = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=form.has_sockets.data,
            has_toilet=form.has_toilet.data,
            has_wifi=form.has_wifi.data,
            can_take_calls=form.can_take_calls.data,
            seats=form.seats.data,
            coffee_price=f"£{format(form.coffee_price.data, '.2f')}"
        )
        db.session.add(new)
        db.session.commit()
        return redirect("/add")
    return render_template("add.html", form=form)


@app.route("/delete/<cafe_name>", methods=["GET", "POST"])
def delete(cafe_name):
    cafe_to_del = db.one_or_404((db.select(Cafe).filter_by(name=cafe_name)))
    db.session.delete(cafe_to_del)
    db.session.commit()
    return redirect(url_for("cafe_names"))


if __name__ == "__main__":
    app.run(debug=True)
