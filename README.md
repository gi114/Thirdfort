# Thirdfort Coding Challenge

## How to run:

1. Clone the repo with ```git clone https://github.com/gi114/Thirdfort```
2. Make a virtual environment
3. Install dependencies with ```pip install -r requirements.txt```
4. Set an environment variable to the flask application file by typing ```export FLASK_APP=main.py```
    If you are on windows, substitute `export` with `set`
5. Run the application with ```python main.py```
6. This step will run the web server. Navigate to the localhost address provided and add path `/login` or `/register`
7. You can now sign in and use the app!

## Instructions to the UX team

The `/index` route takes to the main page for each user where the list his/her personal notes are show. 
In the main page, users can add and save new notes. By clicking on each note, user navigate on a page specific to that note.
The corresponding route is built dynamically using the note ID. In such page, the user can modify the given note by either 
deleting it, archiving it or updating it.

The `/archived` route takes to the page of archived notes. By clicking on each archived note, which is again built
using dynamic routes, the user can unarchive the given note

Through the app, links to `login`, `index` and `archived` pages ara available

Each route function in the `main.py` file has a corresponding `html` file that it renders to enable data visualization.
Such rendering uses the structure provided by Flask forms, also available in each function (imported from `forms.py`)

## Technology choices

Following good coding practices I decided to use a web framework to develop the app. I considered the possibility of using
Django but, given the time constraint for this exercise, my final choice was for Flask due to its lightweight and minimal set up and its integrated unit-tests
support. In addition, Flask is known to be better performant than Django and it provides an easy NoSQL integration.


## What would I change and add it had more time

There is a number of features that must be added to a fully functioning API. Therefore, I would

- Improve field validation, particularly for login and registration
- Improve the app security generating a truly random key with `os.urandom()` function or better, a true random number generator
- Improve html and CSS to provide users with a complete UI (logos, user profile pic)
- Add rules to manage notes ID and enable reusing ID of deleted notes
- Display notes by timestamps (most recent first)
- Add a database to manage multiple users, save posts and updates
