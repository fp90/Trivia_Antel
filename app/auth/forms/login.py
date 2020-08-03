from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length, Email, AnyOf


# Formulario para el login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        InputRequired('El campo no puede ser vacio'),
        Email('Formato incorrecto')])

    password = PasswordField('Password', validators=[
        InputRequired('El campo no puede ser vacio')])

    remember_me = BooleanField('Recuérdame')

    submit = SubmitField('Login')
