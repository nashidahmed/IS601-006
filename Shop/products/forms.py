from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TextAreaField, IntegerField, URLField, SubmitField, BooleanField, DecimalField, SelectField
from wtforms.validators import DataRequired, Length, Optional, NumberRange

class ProductForm(FlaskForm):
    id = HiddenField("id", validators=[Optional()])
    name = StringField("name", validators=[DataRequired(), Length(max=30)])
    description = TextAreaField("description", validators=[DataRequired()])
    category = SelectField("category", validators=[DataRequired()], choices=[('', 'Pick category...')])
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
    category = SelectField("category", choices=[('', 'Pick category...')])
    col = SelectField("sort by", choices=[('', 'Pick attribute...'), ('name', 'Name'), ('cost', 'Cost')])
    order = SelectField("Order", choices=[('', 'Choose...'), ('asc', 'Ascending'), ('desc', 'Descending')])
    submit = SubmitField("Filter")
