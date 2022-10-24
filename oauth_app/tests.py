from django.test import TestCase
import requests


# Create your tests here.

class GoogleLoginTestCases(TestCase):

    def test_login_successful(self):
        req = requests.get("https://uva-cs3240-b-24.herokuapp.com/")
        self.assertEqual(req.status_code, 200)
