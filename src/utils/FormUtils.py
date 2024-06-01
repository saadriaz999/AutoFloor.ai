from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class Step1Form(FlaskForm):
    rooms = IntegerField('Rooms', validators=[DataRequired()])
    next = SubmitField('Next')


class Step2Form(FlaskForm):
    bathrooms = IntegerField('Bathrooms', validators=[DataRequired()])
    next = SubmitField('Next')


class Step3Form(FlaskForm):
    garage = BooleanField('Garage')
    submit = SubmitField('Submit')


class Step4Form(FlaskForm):
    kitchen = BooleanField('Kitchen')
    submit = SubmitField('Submit')


class Step5Form(FlaskForm):
    prompt = StringField('Prompt', validators=[DataRequired()])
    submit = SubmitField('Submit')
