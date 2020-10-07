# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request, jsonify, render_template
from forms import RegistrationForm, LoginForm
from config import Config
app = Flask(__name__)
app.config.from_object(Config)


archived_notes = [
    {'id': 4,
     'note': 'forth note',
     'timestamp': '09:14:55'},
    {'id': 5,
     'note': 'fifth note',
     'timestamp': '23:25:60'}
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


@app.route('/register')
def register():
    # create an instance of a form
    form = RegistrationForm
    return render_template('registration.html', title='Sign up', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Giulia'}
    return render_template('index.html', title='Home', user=user, posts=saved_notes)


# A route to return all of the available entries in our catalog.
@app.route('/saved_notes', methods=['GET'])
def list_saved_notes():
    return jsonify(saved_notes)


@app.route('/archived_notes', methods=['GET'])
def list_archived_notes():
    return jsonify(archived_notes)


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