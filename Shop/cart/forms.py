from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TextAreaField, IntegerField, URLField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, NumberRange

class CartForm(FlaskForm):
    id = HiddenField("id", validators=[Optional()])
    quantity = IntegerField("quantity", validators=[DataRequired(), NumberRange(min=1, message='Select at least 1')])
    product_id = HiddenField("product_id", validators=[Optional()])

class AddForm(CartForm):
    submit = SubmitField("Add to cart")
