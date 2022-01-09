from django.test import TestCase, RequestFactory
from django.test import Client
from accounts.forms import CreateUserForm
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.models import Group
from accounts.views import registerPage, editUserPage, loginPage
from django.contrib.sessions.middleware import SessionMiddleware
from .forms import CreateUserForm, LoginForm, UpdateUserForm
# from django.test import LiveServerTestCase
# from selenium.webdriver.chrome.webdriver import WebDriver
# import time


class AccountsTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        researcher = Group(name = "researcher")
        staff = Group(name = "staff")
        staff.save()
        researcher.save()
        cls.user = User.objects.create_user(username = 'john', password='johnpassword')
        cls.admin_staff = User.objects.create_user(username='admin', password='adminpassword')
        cls.admin_staff.groups.add(staff)
        cls.user.groups.add(researcher)
        cls.factory = RequestFactory()

 

    def testNoAllInput(self):

        #No email

        data = {'first_name': 'Test', 'last_name': 'Test', 'username': "Test", 'password1': 'POL123@4', 'password2': 'POL123@4'}

        form = CreateUserForm(data)

        self.assertFalse(form.is_valid(), "The test did not pass")

        #no firstname

        data = {'last_name': 'Test', 'username': "Test", 'email': 'hello@gmail.com', 'password1': 'POL123@4', 'password2': 'POL123@4'}

        form = CreateUserForm(data)

        self.assertFalse(form.is_valid(), "The test did not pass")

        #no lastname

        data = {'first_name': 'Test', 'username': "Test", 'email': 'hello@gmail.com', 'password1': 'POL123@4', 'password2': 'POL123@4'}

        form = CreateUserForm(data)

        self.assertFalse(form.is_valid(), "The test did not pass")


        # No password

        data = {'first_name': 'Test', 'username': "Test", 'email': 'hello@gmail.com'}

        form = CreateUserForm(data)

        self.assertFalse(form.is_valid(), "The test did not pass")

        
    def testWrongPassword(self):

        #wrong password format

        #less than 8 character
        data = {'first_name': 'Test','last_name': 'Test', 'username': "Test", 'email': 'hello@gmail.com', 'password1': 'admin', 'password2': 'admin'}

        form = CreateUserForm(data)

        self.assertFalse(form.is_valid(), "The test did not pass")


        #entire number
        data = {'first_name': 'Test','last_name': 'Test', 'username': "Test", 'email': 'hello@gmail.com', 'password1': '12345213', 'password2': '12345213'}

        form = CreateUserForm(data)

        self.assertFalse(form.is_valid(), "The test did not pass")


        


    def testCorrectPasswordFormat(self):

        data = {'first_name': 'Test','last_name': 'Test', 'username': "Test", 'email': 'hello@gmail.com', 'password1': 'POL123@4', 'password2': 'POL123@4'}

        form = CreateUserForm(data)

        self.assertTrue(form.is_valid(), "The test did not pass")

    
    def testWrongEmail(self):

        data = {'first_name': 'Test','last_name': 'Test', 'username': "Test", 'email': 'hellogmail.com', 'password1': 'POL123@4', 'password2': 'POL123@4'}

        form = CreateUserForm(data)

        self.assertFalse(form.is_valid(), "The test did not pass")

        data = {'first_name': 'Test','last_name': 'Test', 'username': "Test", 'email': 'hello@gmail', 'password1': 'POL123@4', 'password2': 'POL123@4'}

        form = CreateUserForm(data)

        self.assertFalse(form.is_valid(), "The test did not pass")

        data = {'first_name': 'Test','last_name': 'Test', 'username': "Test", 'email': '.e8lo@gmail', 'password1': 'POL123@4', 'password2': 'POL123@4'}

        form = CreateUserForm(data)

        self.assertFalse(form.is_valid(), "The test did not pass")

    def testCorrectEmail(self):

        data = {'first_name': 'Test','last_name': 'Test', 'username': "Test", 'email': 'hello@gmail.com', 'password1': 'POL123@4', 'password2': 'POL123@4'}

        form = CreateUserForm(data)

        self.assertTrue(form.is_valid(), "The test did not pass")


    def testWrongUsername(self):

        data = {'first_name': 'Test','last_name': 'Test', 'username': "Tes^t?", 'email': 'hello@gmail.com', 'password1': 'POL123@4', 'password2': 'POL123@4'}

        form = CreateUserForm(data)

        self.assertFalse(form.is_valid(), "The test did not pass")

    def testCorrectUsername(self):

        data = {'first_name': 'Test','last_name': 'Test', 'username': "Tes23t@.+-_", 'email': 'hello@gmail.com', 'password1': 'POL123@4', 'password2': 'POL123@4'}

        form = CreateUserForm(data)

        self.assertTrue(form.is_valid(), "The test did not pass")



        



    # Test whether a researcher can register successfully. It test the user data, also the redirct of the register page


    def test_registePage_wrongpost1(self):

        data = {'first_name': 'Test','last_name': 'Test', 'username': "Test", 'email': 'hello@gmail', 'password1': '123456', 'password2': '123456'}

        request = self.factory.post('/register/', data, follow=True)

        request.user = AnonymousUser()

        response = registerPage(request)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response=response, text='''<title>Register</title>''', html=True)

        self.assertEqual(len(User.objects.filter(username="Test")), 0)

    def test_registePage_wrongpost2(self):

        data = {'first_name': 'Test','last_name': 'Test', 'username': "Test", 'email': 'hellogmail.com', 'password1': '123456', 'password2': '123456'}

        request = self.factory.post('/register/', data, follow=True)

        request.user = AnonymousUser()

        response = registerPage(request)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response=response, text='''<title>Register</title>''', html=True)

        self.assertEqual(len(User.objects.filter(username="Test")), 0)

        
        
        




    def test_registerPage_post1(self):

        data = {'first_name': 'Test','last_name': 'Test', 'username': "T1st+-", 'email': 'hello@gmail.com', 'password1': 'POL123@45', 'password2': 'POL123@45'}

        request = self.factory.post('/register/', data, follow=True)

        request.user = AnonymousUser()

        response = registerPage(request)

        self.assertEqual(response.headers['Location'], '/login/')
        self.assertEqual(response.status_code, 302)

        testers = User.objects.filter(username="T1st+-")

        self.assertEqual(len(testers), 1)
        self.assertEqual(testers[0].first_name, "Test")
        self.assertEqual(testers[0].last_name, "Test")
        self.assertEqual(testers[0].email, 'hello@gmail.com')
        self.assertEqual(testers[0].groups.all()[0].name, 'researcher')
    
    def test_registerPage_post2(self):

        data = {'first_name': 'Test','last_name': 'Test', 'username': "T1st+-", 'email': 'hello@gmail.com', 'password1': 'POL123@4', 'password2': 'POL123@4'}

        request = self.factory.post('/register/', data, follow=True)

        request.user = AnonymousUser()

        response = registerPage(request)

        self.assertEqual(response.headers['Location'], '/login/')
        self.assertEqual(response.status_code, 302)

        testers = User.objects.filter(username="T1st+-")

        self.assertEqual(len(testers), 1)
        self.assertEqual(testers[0].first_name, "Test")
        self.assertEqual(testers[0].last_name, "Test")
        self.assertEqual(testers[0].email, 'hello@gmail.com')
        self.assertEqual(testers[0].groups.all()[0].name, 'researcher')

    


    def test_registerPage_get(self):

        response = self.client.get('/register/')
        
        # Test contexts
        self.assertIsInstance(response.context['form'], CreateUserForm)

        request = self.factory.get('/register/')

        request.user = AnonymousUser()

        response = registerPage(request)

        self.assertEqual(response.status_code, 200)


        

    
    def test_editUserPage_post(self):

        data = {'first_name': 'change','last_name': 'change', 'username': "change", 'email': 'change@gmail.com'}

        request = self.factory.post('/edit_profile/', data, follow = True)
        request.user = self.user

        response = editUserPage(request)


        self.assertEqual(response.headers['Location'], '/coversheet/edit_profile/')
        self.assertEqual(response.status_code, 302)

        

        self.assertEqual(self.user.first_name, "change")
        self.assertEqual(self.user.last_name, "change")
        self.assertEqual(self.user.email, 'change@gmail.com')
        self.assertEqual(self.user.groups.all()[0].name, 'researcher')

        





    
    def test_editUserPage_get(self):

        request = self.factory.get('/edit_profile/')

        request.user = self.user

        response = editUserPage(request)

        self.assertEqual(response.status_code, 200)


    



    def test_login1(self):
        

        data = {'username': "admin", 'password': 'adminpassword', 'remember_me': False}

        request = self.factory.post('/login/', data)

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        

        request.user = AnonymousUser()

        response = loginPage(request)

        self.assertEqual(response.headers['Location'], '/approvelist/')
        self.assertEqual(response.status_code, 302)


    def test_login2(self):

        data = {'username': "john", 'password': 'johnpassword', 'remember_me': False}

        request = self.factory.post('/login/', data)

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        request.user = AnonymousUser()

        response = loginPage(request)

        self.assertEqual(response.headers['Location'], '/managelist/')
        self.assertEqual(response.status_code, 302)

    
    def test_login3(self):

        other = User.objects.create_user(username = 'test', password='testpassword')

        data = {'username': "test", 'password': 'testpassword', 'remember_me': False}

        request = self.factory.post('/login/', data)

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = AnonymousUser()
        response = loginPage(request)

        #self.assertEqual(response.headers['Location'], '/login/')
        self.assertEqual(response.status_code, 200)
       

    def test_login4(self):

        request = self.factory.get('/login')
        request.user = AnonymousUser()
        response = loginPage(request)
        self.assertEqual(response.status_code, 200)

    
    










        





    

























        # response = self.
        
        # self.assertFormError(response, 'form', 'username', 'username must be 150 characters or fewer, must contain letters, digits and @/./+/-/_ only')

#     def testAnswer(self):
#         pass


#     def testQuestion(self):
#         pass


# class SimpleTest(TestCase):
    
    
#     def test_register(self):
#         response = self.client.get('/register/')
#         self.assertEqual(response.status_code, 200)





# class MySeleniumTests(LiveServerTestCase):

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         group = Group.objects.
#         cls.selenium = WebDriver(executable_path = '/Users/alvinpeng/Desktop/chromedriver')
#         cls.selenium.implicitly_wait(10)



#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super().tearDownClass()

#     def test_login(self):

#         time.sleep(3)
#         # test if someone can  login the page
#         self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
#         username_input = self.selenium.find_element_by_name("username")
#         username_input.send_keys('admin')
#         time.sleep(3)
#         password_input = self.selenium.find_element_by_name("password")
#         password_input.send_keys('admin')
#         time.sleep(3)
#         self.selenium.find_element_by_xpath('//*[@id="login"]').click()
#         time.sleep(3)

    



