from django.test import TestCase
from django.db.models import Q
import requests


# Create your tests here.

class GoogleLoginTestCases(TestCase):

    def test_login_successful(self):
        req = requests.get("https://uva-cs3240-b-24.herokuapp.com/")
        self.assertEqual(req.status_code, 200)

   
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
