from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired

class ProcesoForm(FlaskForm):
    nombre = StringField('Nombre del proceso', validators=[DataRequired()])
    costo_unitario = DecimalField('Costo por unidad', validators=[DataRequired()])
    submit = SubmitField('Guardar proceso')
