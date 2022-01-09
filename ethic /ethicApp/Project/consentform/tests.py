from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.models import Group
from accounts.views import loginPage
from .views import Consentform
# Create your tests here.


class consentformTest(TestCase):
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
    def consentformTest1(self):
        request1 = self.factory.post('/login')
        request1.user = self.user
        loginPage(request)
        request2 = self.factory.get('/consentform')
        request2.user = self.user
        Consentform(request2)
        print(request2)

