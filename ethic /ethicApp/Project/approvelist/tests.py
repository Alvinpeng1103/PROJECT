
from django.test import TestCase, RequestFactory
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from accounts.models import Application
from .views import approve, disapprove, approvelistPage

# Create your tests here.

class approvelistTest(TestCase):
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

    def testApprove(self):

        sample = Application(id=1, user = self.user, status = "COMPLETE")

        sample.save()

        self.assertEqual(sample.status, "COMPLETE")

        request = self.factory.get('/approvelist/')

        request.user = self.admin_staff

        response = approve(request=request, item_id=1)

        sample = Application.objects.get(pk=1)

        self.assertEqual(sample.status, "APPROVED")

    
    def testDisapprove(self):

        sample = Application(id=1, user = self.user, status = "COMPLETE")

        sample.save()

        self.assertEqual(sample.status, "COMPLETE")

        request = self.factory.get('/approvelist/')

        request.user = self.admin_staff

        response = disapprove(request=request, item_id=1)

        sample = Application.objects.get(pk=1)

        self.assertEqual(sample.status, "DISAPPROVED")

    
    def testPage(self):

        sample1 = Application(id=1, user = self.user, status = "COMPLETE")
        sample2 = Application(id=2, user = self.user, status = "COMPLETE")
        sample3 = Application(id=3, user = self.user, status = "IN PROGRESS")

        sample1.save()
        sample2.save()
        sample3.save()

        request = self.factory.get('/approvelist/')
        request.user = self.admin_staff
        response = approvelistPage(request=request)


    







    








