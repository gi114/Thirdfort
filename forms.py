from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    """
    Enables new users to register using a form available with flask.
    Applies a number of checks to validate users' inputs
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    """
    Enables existing users to login using a form available with flask.
    Applies a number of checks to validate users' inputs
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class SavedNotesForm(FlaskForm):
    """
    Enables users to update existing saved notes, save new ones, delete or archive them
    """
    #note = TextField(validators=[DataRequired()])
    new_note = StringField('Write new note here:', validators=[DataRequired()])
    save = SubmitField('Save')
    #update_note = StringField('Update note here:', validators=[DataRequired()])
    #update = SubmitField('Update')
    #archive = SubmitField('Archive')
    #delete = SubmitField('Delete')


class ArchivedNotesForm(FlaskForm):
    """
    Enables users to unarchive archived notes
    """
    note = TextField(validators=[DataRequired()])
    unarchive = SubmitField('Unarchive')
