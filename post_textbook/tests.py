from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Textbook, Department, Course 

 #dummy test  
class DummyTest(TestCase):
    def testShouldWork(self):
        self.assertTrue(True)

#test the form for a creation of a textbook
class TestTextBook(TestCase):
    #test the putting in a department name in form
    def create_department(self, name="ECE", courses=[], textbooks=[]):
        department= Department.objects.create(name=name)
        test_user =  User.objects.create(username='test user')
        for course in courses:
            c=Course.objects.create(name=course['name'], department=department)
        for textbook in textbooks:
            tb=Textbook.objects.create(department=department, course=c, user=test_user, title=textbook['title'],  author=textbook['author'], publisher=textbook['publisher'],edition=textbook['edition'], year=textbook['year'], ISBN=textbook['ISBN'])
        return department


    #test the when a course is made
    def create_course(self, name= "Fun3", department="ECE"):
        course= Course.objects.create(name=name, department=department)
        return course


    #test a fields of the form when a textbook is made
    def test_create_department(self):
        dep=self.create_department(courses=[{'name': 'Fun3'}], textbooks=[{'title':'Signals and Systems', 'author':'Delong', 'publisher':'Michigan publishing', 'edition' : 1 , 'year' : 2018 , 'ISBN':123456789 }])
        self.assertTrue(isinstance(dep, Department))
        self.assertEqual("ECE", dep.name)
        self.assertEqual("Fun3", dep.courses.all()[0].name)
        self.assertEqual("Signals and Systems", dep.textbooks.all()[0].title)
        self.assertEqual("Delong", dep.textbooks.all()[0].author)
        self.assertEqual("Michigan publishing", dep.textbooks.all()[0].publisher)
        self.assertEqual("Delong", dep.textbooks.all()[0].author)
        self.assertEqual(1, dep.textbooks.all()[0].edition)
        self.assertEqual(2018, dep.textbooks.all()[0].year)
        self.assertEqual(123456789, dep.textbooks.all()[0].ISBN)

    