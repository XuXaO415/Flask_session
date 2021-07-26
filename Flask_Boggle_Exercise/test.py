from unittest import TestCase
from app import app
from flask import Flask, session
# from flask import session
from boggle import Boggle

# Make Flask errors be real errors, not HTML pages with error info
app.config["Testing"] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def setUp(self):
        """Set up test"""
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session["count"] = 999
                res = client.get("/")
                self.assertEqual(res.status_code, 200)
                self.assertEqual(session['count'], 1000)

    # def tearDown(self):

    # def test_homepage(self):
        # def test_1(self):
