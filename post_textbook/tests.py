from django.test import TestCase, Client
from django.conf import settings
from .models import Textbook, Department, Course 

 #dummy test  
class DummyTest(TestCase):
    def testShouldWork(self):
        self.assertTrue(True)

#test the form for a creation of a textbook
class TestTextBook(TestCase):
    #test the putting in a department name in form
    def create_department(self, name='ECE', courses=[]):
        department= Department.objects.create(name=name)
        for course in courses:
            Course.objects.create(name=course['name'], department=department)
        return department



    #test the when a course is made
    def create_course(self, name= "Fun3", department="ECE"):
        # department= Department.objects.create(name= "ECE")
        course= Course.objects.create(name=name, department=department)
        return course

    #test when a textbook is created
    def create_textbook(self, department="ECE", course="Fun3", title="Signals and Systems", author= "Delong", publisher= "Michigan publishing", edition="1", year= "2018", ISBN= " 123456789"):
        test_user = settings.AUTH_USER_MODEL
        textbook = Textbook.objects.create(department=department, course=course, user= test_user, title=title,  author=author, publisher=publisher,edition=edition, year=year, ISBN=ISBN)
        return textbook

    #test a fields of the form when a textbook is made
    def test_create_textbook(self):
        tb=self.create_textbook()
        self.assertEqual("ECE", tb.department)
        self.assertEqual("Fun3", tb.course)
        self.assertEqual("Signals and Systems", tb.title)
        self.assertEqual("Delong", tb.author)
        self.assertEqual("Michigan publishing", tb.publisher)
        self.assertEqual("1", tb.edition)
        self.assertEqual("2018", tb.year)
        self.assertEqual("123456789", tb.ISBN)
        self.assertTrue(isinstance(tb, Textbook))
    
    # def test_create_textbook_view(self):
    #     client= Client()
    #     res=client.get('/create')
    #     self.assertTemplateUsed(res, "post_textbook/create_textbook.html")
  
    

