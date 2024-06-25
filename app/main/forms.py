from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired

class EntryForm(FlaskForm):
    text = TextAreaField('Entry', validators=[DataRequired()])
    image_url = StringField('Image URL')
    submit = SubmitField('Submit')