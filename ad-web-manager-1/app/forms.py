from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, SelectField
from wtforms.validators import DataRequired, Email, Length

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=35)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Add User')

class DeleteUserForm(FlaskForm):
    username = SelectField('Select User', coerce=str, validators=[DataRequired()])
    submit = SubmitField('Delete User')

class BatchAddForm(FlaskForm):
    file = FileField('Upload CSV File', validators=[DataRequired()])
    submit = SubmitField('Batch Add Users')

class BatchDeleteForm(FlaskForm):
    usernames = SelectField('Select Users', coerce=str, multiple=True, validators=[DataRequired()])
    submit = SubmitField('Batch Delete Users')