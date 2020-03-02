from flask_wtf import Form
from wtforms import (
  StringField,
  SelectField
)
from wtforms.validators import Length

class CarForm(Form):
  name = StringField('Name', validators=[Length(max=30)])
  color = SelectField('Color', coerce=str, choices=[
      ('blue', 'Blue'),
      ('red', 'Red')
    ])