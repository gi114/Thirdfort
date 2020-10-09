import pytest
import sys
import os
from forms import RegistrationForm, LoginForm, SaveNoteForm, ModifyNoteForm, ArchivedNoteForm
from flask import Flask
sys.path.append(os.path.abspath(os.path.dirname("__file__")))
try:
    from main import app
    import unittest
except Exception as e:
    print("Missing modules {}".format(e))


class FlaskTest(unittest.TestCase):

    # Check index for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/index")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # Check archived for response 200
    def test_archived(self):
        tester = app.test_client(self)
        response = tester.get("/archived")
        status_code = response.status_code
        self.assertEqual(status_code, 200)


if __name__ == '__main__':
    unittest.main()
