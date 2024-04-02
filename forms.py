from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, URLField, FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired


class AddCafe(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    map_url = URLField('Google maps link', validators=[DataRequired()])
    img_url = URLField('Picture', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    has_sockets = BooleanField('Sockets')
    has_toilet = BooleanField('Toilet')
    has_wifi = BooleanField('Wifi')
    can_take_calls = BooleanField('Calls')
    seats = SelectField('Seats', choices=["0-10", "10-20", "20-30", "30-40", "40-50", "50+"])
    coffee_price = FloatField('Price')
    submit = SubmitField()












