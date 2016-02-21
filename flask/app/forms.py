from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class LoginForm(Form):
    name = StringField('Name', validators=[DataRequired()])
