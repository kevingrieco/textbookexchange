from django.test import TestCase
from .models import Textbook
from django.urls import reverse

class QuestionIndexViewTests(TestCase):
    def test_no_textbooks(self):
        """
        If no textbook exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('templates:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No textbooks are available.")
        self.assertQuerysetEqual(response.context['current_textbooks'], [])