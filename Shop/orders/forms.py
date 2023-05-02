from flask_wtf import FlaskForm
from wtforms import HiddenField, DecimalField, SubmitField, StringField, RadioField
from wtforms.validators import DataRequired, Length, Optional, NumberRange, Regexp

# nn379 Apr 30 2023
class PaymentForm(FlaskForm):
    id = HiddenField("id", validators=[Optional()])
    first_name = StringField("first name", validators=[DataRequired()])
    last_name = StringField("last name", validators=[DataRequired()])
    amount = DecimalField("payment amount", validators=[DataRequired(), NumberRange(min=0)])
    method = RadioField("payment method", validators=[DataRequired()], choices=[('CASH', 'Cash on Delivery'), ('DEBIT_CARD', 'Debit Card'), ('CREDIT_CARD', 'Credit card')])
    street_address = StringField("street address", validators=[DataRequired()])
    city = StringField("city", validators=[DataRequired()])
    zip = StringField("zip", validators=[DataRequired(),Length(min=5, max=6),Regexp('^\?[0-9]$', message="Zip code should be numeric with 5-6 digits")])
    state = StringField("state", validators=[DataRequired()])
    country = StringField("country", validators=[DataRequired()])
    submit = SubmitField("Confirm purchase")