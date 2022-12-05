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
    def create_department(self, name="ECE"):
        department= Department.objects.create(name=name)
        return department

    #test the when a course is made
    def create_course(self, name= "Fun3", dep=[]):
        department= Department.objects.create(name= dep['name'])
        course= Course.objects.create(name=name, department=department)
        return course

    #test when a textbook is created
    def create_textbook(self, department=[], course=[], title="Signals and Systems", author= "Delong", publisher= "michigan publishing", edition="1", year= "2018", ISBN= " 123456789"):
        test_user = settings.AUTH_USER_MODEL
        department= Department.objects.create(name= department['name'])
        textbook = Textbook.objects.create(department=department, user= test_user, title=title,  author=author, publisher=publisher,edition=edition, year=year, ISBN=ISBN)
        for courseInfo in course:
            Course.objects.create(name=courseInfo['name'], department=department)
        return textbook

    #test a fields of the form when a textbook is made
    def test_create_textbook(self):
        tb=self.create_textbook(department=[{'name':'CS'}], course=[{'name':'Data structures'}])
        self.assertEqual("CS", tb.department.all()[0].name)
        self.assertEqual("Data structures", tb.course.all()[0].name)
        self.assertTrue(isinstance(tb, Textbook))
        self.assertEqual("Signals and Systems", tb.title)
        self.assertEqual("delong", tb.author)
        self.assertEqual("michigan publishing", tb.publisher)
        self.assertEqual("1", tb.edition)
        self.assertEqual("2018", tb.year)
        self.assertEqual("123456789", tb.ISBN)
    
    # def test_create_textbook_view(self):
    #     client= Client()
    #     res=client.get('/create')
    #     self.assertTemplateUsed(res, "post_textbook/create_textbook.html")
  
    

