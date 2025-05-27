from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange

class PersonalizacionForm(FlaskForm):
    descripcion = StringField('Descripción', validators=[DataRequired()])
    posicion = IntegerField('Posición (1–10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    proceso = SelectField('Proceso', choices=[], coerce=str)  # se llenará en la vista
    precio = DecimalField('Precio', validators=[DataRequired()])
    submit = SubmitField('Agregar personalización')
