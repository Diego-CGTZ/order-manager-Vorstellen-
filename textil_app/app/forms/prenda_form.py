from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired

class PrendaForm(FlaskForm):
    tipo = StringField('Tipo de prenda', validators=[DataRequired()])
    cantidad = IntegerField('Cantidad', validators=[DataRequired()])
    precio_unitario = DecimalField('Precio unitario', validators=[DataRequired()])
    # Aquí podemos insertar personalizaciones con JavaScript dinámicamente
    submit = SubmitField('Guardar prenda')
