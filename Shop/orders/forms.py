from flask_wtf import FlaskForm
from wtforms import HiddenField, DecimalField, TextAreaField, SubmitField, StringField, RadioField
from wtforms.validators import DataRequired, Length, Optional, NumberRange

class PaymentForm(FlaskForm):
    id = HiddenField("id", validators=[Optional()])
    first_name = StringField("first name", validators=[DataRequired()])
    last_name = StringField("last name", validators=[DataRequired()])
    amount = DecimalField("amount", validators=[DataRequired(), NumberRange(min=0)])
    method = RadioField("payment method", validators=[DataRequired()], choices=[('CASH', 'Cash on Delivery'), ('DEBIT_CARD', 'Debit Card'), ('CREDIT_CARD', 'Credit card')])
    address = TextAreaField("address", validators=[DataRequired()])
    submit = SubmitField("Confirm purchase")