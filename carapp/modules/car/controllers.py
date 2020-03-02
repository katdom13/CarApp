from flask import (
  Blueprint,
  render_template,
  request,
  redirect,
  url_for
)
from carapp.models import Car
from carapp.forms import CarForm
car = Blueprint('car', __name__, url_prefix='/car')

@car.route('/cars', methods=['GET', 'POST'])
def show():
  form = CarForm()
  cars = Car.query.all()
  car_list = []
  for car in cars:
    car_list.append(car.to_dict())
  return render_template('pages/car/cars.html', cars=car_list, form=form)


@car.route('/car/add', methods=['POST'])
def add():
  name = request.form.get('name')
  color = request.form.get('color')

  _car = Car(name=name, color=color)
  
  try:
    _car.save()
    flash('Added car')
  except:
    flash('Error adding car')
  finally:
    return redirect(url_for('car.show'))


@car.route('/car/<car_id>/delete', methods=['POST'])
def delete(car_id):
  _car = Car.find_by_identity(car_id)
  _car.delete()
  return redirect(url_for('car.show'))