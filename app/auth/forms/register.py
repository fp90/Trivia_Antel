from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length


class RegisterForm(FlaskForm):
    username = StringField(  'Nombre de Usuario', validators=[
        DataRequired('El campo no puede ser vacio')])

    email = StringField(  'Email',validators=[
        DataRequired('El campo no puede ser vacio'),
        Email('Formato incorrecto')])

    password = PasswordField('Contraseña', validators=[
        DataRequired('El campo no puede ser vacio'),
        Length(min=4, message='La contraseña debe contener al menos 4 caracteres')])

    password2 = PasswordField('Repita su Contraseña', validators=[
        DataRequired('El campo no puede ser vacio'),
        EqualTo('password', 'Las contraseñas no coinciden')])

    submit = SubmitField('Registro')
