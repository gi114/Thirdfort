# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request, jsonify, render_template, flash, redirect
from forms import RegistrationForm, LoginForm
from config import Config
app = Flask(__name__)
app.config.from_object(Config)


archived_notes = [
    {'id': 3,
     'note': 'forth note',
     'timestamp': '11:44:06'},
    {'id': 4,
     'note': 'fifth note',
     'timestamp': '01:39:00'}
]
saved_notes = [
    {'id': 0,
     'note': 'first note',
     'timestamp': '12:04:00'},
    {'id': 1,
     'note': 'second note',
     'timestamp': '13:09:00'},
    {'id': 2,
     'title': 'third note',
     'timestamp': '19:45:30'}
]


@app.route('/register', methods=['GET', 'POST'])
def register():
    # create an instance of a form
    form = RegistrationForm()
    # TODO: if already registered redirect to login
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect('/index')
    return render_template('register.html', title='Sign Up', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # TODO: if never registered redirect to register
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect('/index')
    return render_template('login.html', title='Login', form=form)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Giulia'}
    return render_template('index.html', title='Home - Saved Notes', user=user, posts=saved_notes)


@app.route('/archived', methods=['GET'])
def archived():
    user = {'username': 'Giulia'}
    return render_template('archived.html', title='Home - Archived Notes', user=user, posts=archived_notes)


# A route to return all of the available entries in our catalog.
@app.route('/notes', methods=['GET'])
def delete_note():
    return jsonify(saved_notes)


# A route to return all of the available entries in our catalog.
@app.route('/notes', methods=['GET'])
def save_note():
    return jsonify(saved_notes)


# A route to return all of the available entries in our catalog.
@app.route('/notes', methods=['GET'])
def update_note():
    return jsonify(saved_notes)


# A route to return all of the available entries in our catalog.
@app.route('/notes', methods=['GET'])
def archive_note():
    return jsonify(saved_notes)


# A route to return all of the available entries in our catalog.
@app.route('/notes', methods=['GET'])
def unarchived_note():
    return jsonify(saved_notes)



if __name__ == '__main__':
    app.run(debug=True)