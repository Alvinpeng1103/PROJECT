from django.test import TestCase, RequestFactory
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from accounts.models import Application
from managelist.views import managelistPage, deleteRow

# Create your tests here.

class ManagelistTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        researcher = Group(name = "researcher")
        researcher.save()
        cls.user = User.objects.create_user(username = 'john', password='johnpassword')
        cls.user.groups.add(researcher)
        cls.factory = RequestFactory()
    
    

    def test_no_login(self):

        # you can not directly access the managelist page

        response = self.client.get('/managelist/', follow=True)
        self.assertEqual(response.status_code, 200)

    # def test_login(self):
    #     c = Client()

    #     response = c.post('/login/', {'username': 'john', 'password': 'johnpassword'}, follow=True)

    #     self.assertEqual(response.status_code, 200)

    #     self.assertEqual(response.redirect_chain[0][0], '/managelist/', "The page did not redirct to the managelist page")
    #     self.assertEqual(response.redirect_chain[0][1], 302, "The page did not redirct to the managelist page")

        
    def test_application(self):

    
        new_application = Application.objects.create(id = 1, user=self.user, status = "IN PROGRESS", supervisor="Alvin", title="Test")
        c = Client()
        response = c.post('/login/', {'username': 'john', 'password': 'johnpassword'}, follow=True)

        applications = response.context['applications']

        instance = applications.get(pk=1)

        self.assertEqual(instance.status, "IN PROGRESS")
        self.assertEqual(instance.title, "Test")
        self.assertEqual(instance.supervisor, "Alvin")

    
    def test_getPage(self):

        request = self.factory.get('/managelist/')

        request.user = self.user

        response = managelistPage(request)

        self.assertEqual(response.status_code, 200)


    def test_delete(self):

        new_application = Application.objects.create(id = 1, user=self.user, status = "IN PROGRESS", supervisor="Alvin", title="Test")
        request = self.factory.get('/managelist/')
        request.user = self.user        
        response = managelistPage(request)
        app_id = '''<td>1</td>'''
        app_name = '''<td>Test</td>'''
        app_status = '''<td>IN PROGRESS</td>'''
        app_supervisor = '''<td>Alvin</td>'''
        self.assertContains(response=response, text=app_id, html=True)
        self.assertContains(response=response, text=app_name, html=True)
        self.assertContains(response=response, text=app_status, html=True)
        self.assertContains(response=response, text=app_supervisor, html=True)
       
        response2 = deleteRow(request, 1)

        self.assertEqual(response2.url, '/managelist/')
        
        response3 = self.client.post('/login/', {'username': 'john', 'password': 'johnpassword'}, follow=True)
        self.assertNotContains(response=response3, text=app_id, html=True)
        self.assertNotContains(response=response3, text=app_name, html=True)
        self.assertNotContains(response=response3, text=app_status, html=True)
        self.assertNotContains(response=response3, text=app_supervisor, html=True)

        self.assertEqual(len(Application.objects.all()), 0)






    



        




        
        
        response3 = self.client.post('/login/', {'username': 'john', 'password': 'johnpassword'}, follow=True)
        self.assertNotContains(response=response3, text=app_id, html=True)
        self.assertNotContains(response=response3, text=app_name, html=True)
        self.assertNotContains(response=response3, text=app_status, html=True)
        self.assertNotContains(response=response3, text=app_supervisor, html=True)

        self.assertEqual(len(Application.objects.all()), 0)






    



        




        
        






        

    

