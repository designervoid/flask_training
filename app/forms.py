from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')


class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    text = StringField('Text', validators=[DataRequired()])
    submit = SubmitField('Submit')