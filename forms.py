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


class SaveNoteForm(FlaskForm):
    """
    Enables users to add notes to the list of saved notes
    """
    new_note = StringField('Write new note here:', validators=[DataRequired()])
    save = SubmitField('Save')


class ModifyNoteForm(FlaskForm):
    """
    Enables users to update existing saved notes, delete or archive them
    """
    update_note = StringField('Update note here:')
    update = SubmitField('Update')
    archive = SubmitField('Archive')
    delete = SubmitField('Delete')


class ArchivedNoteForm(FlaskForm):
    """
    Enables users to unarchive archived notes
    """
    unarchive = SubmitField('Unarchive')
