"""
Routes
"""
from app import app, db
from flask import render_template, request, redirect, url_for
from app.forms import HousesForm
from app.models import Houses

# root = http://0.0.0.0:5000
# route (cf. hieronder) = subdirectory, bv. route('/index') -> http://0.0.0.0:5000/index

@app.route('/')
@app.route('/index')
@app.route('/hello')   # all deze routes leiden naar de functie hieronder
def index():
    return "Hello world !"

@app.route('/staff')
def staff():
    staffmembers = [
        {'name': 'Olivier', 'email': 'olivier@claerbout.eu'},
        {'name': 'Titus', 'email': 'titus@claerbout.eu'}
    ]
    return render_template('staff.html', staffmembers=staffmembers)

@app.route('/house/overview', methods=['POST', 'GET'])
def houses_overview():
    houses = Houses.query.all()
    return render_template('houses_list.html', houses=houses)

@app.route('/house/insert', methods=['POST', 'GET'])
def house_insert():
    form = HousesForm()
    if form.validate_on_submit():   # iemand heeft formulier ingevuld & op submit geklikt
        new_house = Houses(
            longitude = form.longitude.data,
            latitude = form.latitude.data,
            housing_median_age = form.housing_median_age.data,
            total_rooms = form.total_rooms.data,
            total_bedrooms = form.total_bedrooms.data,
            population = form.population.data,
            households = form.households.data,
            median_income = form.median_income.data,
            median_house_value = form.median_house_value.data,
            ocean_proximity = form.ocean_proximity.data
        )

        db.session.add(new_house)
        db.session.commit()   # hoeft niet per CRUD, kan gebundeld
        return redirect(url_for('houseoverview'))
    return render_template('house_add.html', form=form, title='Voeg huis toe')   #indien geen huis ingevuld, nieuw formulier renderen