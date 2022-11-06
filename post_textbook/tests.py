from django.test import TestCase
from .models import Textbook
from django.urls import reverse

class QuestionIndexViewTests(TestCase):
    def test_textbooks(self):
        """
        If no textbook exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        