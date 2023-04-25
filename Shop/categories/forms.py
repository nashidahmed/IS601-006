from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, NumberRange

class CategoryForm(FlaskForm):
    id = HiddenField("id", validators=[Optional()])
    name = StringField("name", validators=[DataRequired(), Length(max=30)])

class AddCategoryForm(CategoryForm):
    submit = SubmitField("Add category")

class EditCategoryForm(CategoryForm):
    submit = SubmitField("Edit category")
