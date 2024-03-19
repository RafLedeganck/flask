from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app import app, db


class HousesForm(FlaskForm):
    longitude = FloatField(label='Longitude', validators=[DataRequired()])
    latitude = FloatField(label='Latitude')
    housing_median_age = FloatField(label='Median Age')
    total_rooms = FloatField(label='Total rooms')
    total_bedrooms = FloatField(label='Total bedrooms')
    population = FloatField(label='Population')
    households = FloatField(label='Households')
    median_income = FloatField('Median income')
    median_house_value = FloatField('House value')
    ocean_proximity = StringField('Ocean proximity')
    submit = SubmitField('Process house data')
