from django.test import TestCase
from .models import Textbook
from django.db.models import Q
from django.urls import reverse

class QuestionIndexViewTests(TestCase):
    def test_textbooks(self):
        """
        If no textbook exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
class SearchTestCases(TestCase):     
    def title_search(self):
        q = "fjdkslfd"
        object_list = Textbook.objects.filter(
            Q(title__icontains=q)
        )
        self.assertFalse(object_list, f"No results for title {q}")
    
    def author_search(self):
        q = "fjdkslfd"
        object_list = Textbook.objects.filter(
            Q(author__icontains=q)
        )
        self.assertTrue(object_list, f"No results for author {q}") 
        
    def edition_search(self):
        q = "12310932"
        object_list = Textbook.objects.filter(
            Q(edition__icontains=q)
        )
        self.assertTrue(object_list, f"No results for edition {q}")

    def year_search(self):
        q = "12310932"
        object_list = Textbook.objects.filter(
            Q(year__icontains=q)
        )
        self.assertTrue(object_list, f"No results for year {q}")

    def department_search(self):
        q = "djkfddfk"
        object_list = Textbook.objects.filter(
            Q(department__icontains=q)
        )
        self.assertTrue(object_list, f"No results for department {q}")
        
    def course_search(self):
        q = "3291032"
        object_list = Textbook.objects.filter(
            Q(course__icontains=q)
        )
        self.assertTrue(object_list, f"No results for course {q}")
 
    def publisher_search(self):
        q = "fjdsjfdk"
        object_list = Textbook.objects.filter(
            Q(publisher__icontains=q)
        )
        self.assertTrue(object_list, f"No results for publisher {q}")
