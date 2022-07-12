from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class ItemInformationForm(FlaskForm):
    item_name = StringField('Item Name', validators=[DataRequired()])
    item_price = FloatField('Item Price', validators=[DataRequired()])
    item_quantity = IntegerField('Items in Stock', validators=[DataRequired()])
    save_btn = SubmitField('Save')
