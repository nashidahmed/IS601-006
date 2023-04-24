from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TextAreaField, IntegerField, URLField, SubmitField, BooleanField, DecimalField
from wtforms.validators import DataRequired, Length, Optional, NumberRange

class ProductForm(FlaskForm):
    id = HiddenField("id", validators=[Optional()])
    name = StringField("name", validators=[DataRequired(), Length(max=30)])
    description = TextAreaField("description", validators=[DataRequired()])
    stock = IntegerField("stock", validators=[DataRequired(), NumberRange(min=0)])
    cost = DecimalField("cost", validators=[DataRequired(), NumberRange(min=0)])
    image = URLField("image", validators=[Optional()])
    is_visible = BooleanField("Is Visible")

class AddProductForm(ProductForm):
    submit = SubmitField("Add product")

class EditProductForm(ProductForm):
    submit = SubmitField("Edit product")

class SearchForm(FlaskForm):
    search = StringField("search", validators=[Optional()])
    col = StringField("col", validators=[Optional()])
    order = StringField("order", validators=[Optional()])
    submit = SubmitField("Filter")
