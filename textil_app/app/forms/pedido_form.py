from flask_wtf import FlaskForm
from wtforms import DateField, DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired

class PedidoForm(FlaskForm):
    cliente = SelectField('Cliente', choices=[], coerce=str)  # IDs en choices
    fecha_entrega = DateField('Fecha de entrega', validators=[DataRequired()])
    pago_inicial = DecimalField('Pago inicial', validators=[DataRequired()])
    submit = SubmitField('Crear pedido')
