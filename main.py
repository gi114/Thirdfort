# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request, jsonify, render_template, flash, redirect
from forms import RegistrationForm, LoginForm, SaveNoteForm, ModifyNoteForm, ArchivedNoteForm
from config import Config
from datetime import datetime
now = datetime.now()
app = Flask(__name__)
app.config.from_object(Config)


archived_notes = [
    {'id': 3,
     'note': 'forth note',
     'timestamp': '11:44:06'},
    {'id': 4,
     'note': 'fifth note',
     'timestamp': '01:39:00'},
    {'id': 35,
     'note': 'other note',
     'timestamp': '19:45:30'}
]
saved_notes = [
    {'id': 0,
     'note': 'first note',
     'timestamp': '12:04:00'},
    {'id': 1,
     'note': 'second note',
     'timestamp': '13:09:00'},
    {'id': 2,
     'note': 'third note',
     'timestamp': '19:45:30'},
    {'id': 34,
     'note': 'other note',
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
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SaveNoteForm()
    user = {'username': 'Giulia'}
    if form.validate_on_submit():
        flash('saving new note: {}'.format(
            form.new_note.data))
        new_note = {
            'id': 100,
            'note': str(form.new_note.data),
            'timestamp': now.strftime("%d/%m/%Y %H:%M:%S")
        }
        saved_notes.append(new_note)
        return redirect('/index')
    return render_template('index.html', title='Home - Saved Notes', user=user, posts=saved_notes, form=form)


@app.route('/index/<note_id>', methods=['GET', 'POST'])
def note(note_id):
    form = ModifyNoteForm()
    for saved_note in saved_notes:
        if saved_note['id'] == int(note_id):
            idx = int(saved_notes.index(saved_note))
            title = saved_note['note']
    if form.update.data and form.validate_on_submit():
        flash('updating new note: {}'.format(
            form.update_note.data))
        if len(form.update_note.data) > 0:
            saved_notes[idx]['note'] = form.update_note.data
        return redirect('/index')
    elif form.delete.data and form.validate_on_submit():
        flash('deleting note: {}'.format(
            saved_notes[idx]['note']))
        saved_notes.pop(idx)
        return redirect('/index')
    elif form.archive.data and form.validate_on_submit():
        flash('archiving note: {}'.format(
            saved_notes[idx]['note']))
        to_be_archived = saved_notes.pop(idx)
        archived_notes.append(to_be_archived)
        return redirect('/archived')
    return render_template('note.html', title=title, form=form)


@app.route('/archived', methods=['GET', 'POST'])
def archived():
    user = {'username': 'Giulia'}
    return render_template('archived.html', title='Home - Archived Notes', user=user, posts=archived_notes)


@app.route('/archived/<note_id>', methods=['GET', 'POST'])
def archived_note(note_id):
    form = ArchivedNoteForm()
    for archived_note in archived_notes:
        if archived_note['id'] == int(note_id):
            idx = int(archived_notes.index(archived_note))
            title = archived_note['note']
    if form.validate_on_submit():
        to_be_saved = archived_notes.pop(idx)
        saved_notes.append(to_be_saved)
        return redirect('/archived')
    return render_template('unarchive.html', title=title, form=form)


if __name__ == '__main__':
    app.run(debug=True)