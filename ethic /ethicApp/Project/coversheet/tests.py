from django.test import TestCase, RequestFactory
from django.test import Client
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.models import Group
from coversheet.views import coversheetPage
from accounts.models import Application
from accounts.models import CoverSheetQuestion, CoverSheetAnswers
from qualifier.views import success


# Create your tests here.


class CoversheetTest(TestCase):

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

        CoverSheetQuestion.objects.bulk_create([

            CoverSheetQuestion(question_num=1001, text = 'Provide a lay summary of the project:', is_short_answer=1),
            CoverSheetQuestion(question_num=1002, text = 'Protocol Title:', is_short_answer=1),
            CoverSheetQuestion(question_num=1003, text = 'First Named Chief Investigator Name:', is_short_answer=1),
            CoverSheetQuestion(question_num=1004, text = 'First Named Chief Investigator ID:', is_short_answer=1),
            CoverSheetQuestion(question_num=1005, text = 'School/Centre', is_short_answer=0),
            CoverSheetQuestion(question_num=1006, text = 'Role', is_short_answer=1),
            CoverSheetQuestion(question_num=1007, text = 'Other Internal Investigators Involved:', is_short_answer=0),
            CoverSheetQuestion(question_num=1008, text = 'Number of Internal Investigators (including Chief Investigator):', is_short_answer=0),
            CoverSheetQuestion(question_num=1009, text = 'Other External Investigators Involved:', is_short_answer=0),
            CoverSheetQuestion(question_num=1010, text = 'Number of External Investigators:', is_short_answer=0),
            CoverSheetQuestion(question_num=1011, text = 'Responsible:', is_short_answer=1),
            CoverSheetQuestion(question_num=1012, text = 'Current State:', is_short_answer=1),
            CoverSheetQuestion(question_num=1013, text = 'HREC name:', is_short_answer=1),
            CoverSheetQuestion(question_num=1014, text = 'Action:', is_short_answer=1),
            CoverSheetQuestion(question_num=1015, text = 'Title:', is_short_answer=1),
            CoverSheetQuestion(question_num=1016, text = 'Action:', is_short_answer=1),
            CoverSheetQuestion(question_num=1017, text = 'Please provide any other relevant details:', is_short_answer=1),
        ])

    



    
    def test_coversheet(self):

        data = {'summary': 'test', "protocol": "test", "investigatorname": "Alvin",
         'investigatorid': "1", 'center': '1', 'role': 'chiefinvestigator',
         'otherinternalinvestigators': 'No', 'internalinvestigatorsnumber': '1',
         'otherexternalinvestigators': 'No', 'externalinvestigatorsnumber': '1',
         'responsible': '1', 'currentstate': '1', 'HRECname': '1', 
         'action': '1', 'title': '1', 'contractaction': '1', 'otherrelevantdetails': '1'}


        request1 = self.factory.post('/qualifier/success')

        request1.user = self.user

        response1 = success(request1)

        request2 = self.factory.post('/coversheet/1', data)

        request2.user = self.user

        response2 = coversheetPage(request2, 1)




        self.assertEqual(response2.url, "/questionnaire/1")

        
        answers = CoverSheetAnswers.objects.filter(application_id = 1)

        answer1 = answers.get(question_id=1001)
        answer2 = answers.get(question_id=1002)
        answer3 = answers.get(question_id=1003)
        answer4 = answers.get(question_id=1004)
        answer5 = answers.get(question_id=1005)
        answer6 = answers.get(question_id=1006)
        answer7 = answers.get(question_id=1007)
        answer8 = answers.get(question_id=1008)
        answer9 = answers.get(question_id=1009)
        answer10 = answers.get(question_id=1010)
        answer11 = answers.get(question_id=1011)
        answer12 = answers.get(question_id=1012)
        answer13 = answers.get(question_id=1013)
        answer14 = answers.get(question_id=1014)
        answer15 = answers.get(question_id=1015)
        answer16 = answers.get(question_id=1016)
        answer17 = answers.get(question_id=1017)

        self.assertEqual(answer1.text, "test")
        self.assertEqual(answer2.text, "test")
        self.assertEqual(answer3.text, "Alvin")
        self.assertEqual(answer4.text, "1")
        self.assertEqual(answer5.text, "1")
        self.assertEqual(answer6.text, "chiefinvestigator")
        self.assertEqual(answer7.text, "No")
        self.assertEqual(answer8.text, "1")
        self.assertEqual(answer9.text, "No")
        self.assertEqual(answer10.text, "1")
        self.assertEqual(answer11.text, "1")
        self.assertEqual(answer12.text, "1")
        self.assertEqual(answer13.text, "1")
        self.assertEqual(answer14.text, "1")
        self.assertEqual(answer15.text, "1")
        self.assertEqual(answer16.text, "1")
        self.assertEqual(answer17.text, "1")

        modified = {'summary': 'change', "protocol": "change", "investigatorname": "Alvin",
         'investigatorid': "1", 'center': '1', 'role': 'chiefinvestigator',
         'otherinternalinvestigators': 'No', 'internalinvestigatorsnumber': '1',
         'otherexternalinvestigators': 'No', 'externalinvestigatorsnumber': '1',
         'responsible': '1', 'currentstate': '1', 'HRECname': '1', 
         'action': '1', 'title': '1', 'contractaction': '1', 'otherrelevantdetails': '1'}

        request3 = self.factory.post('/coversheet/1', modified)

        request3.user = self.user

        response3 = coversheetPage(request3, 1) 

        self.assertEqual(response3.url, "/questionnaire/1")



        
        answers = CoverSheetAnswers.objects.filter(application_id = 1)

        answer1 = answers.get(question_id=1001)
        answer2 = answers.get(question_id=1002)
        answer3 = answers.get(question_id=1003)
        answer4 = answers.get(question_id=1004)
        answer5 = answers.get(question_id=1005)
        answer6 = answers.get(question_id=1006)
        answer7 = answers.get(question_id=1007)
        answer8 = answers.get(question_id=1008)
        answer9 = answers.get(question_id=1009)
        answer10 = answers.get(question_id=1010)
        answer11 = answers.get(question_id=1011)
        answer12 = answers.get(question_id=1012)
        answer13 = answers.get(question_id=1013)
        answer14 = answers.get(question_id=1014)
        answer15 = answers.get(question_id=1015)
        answer16 = answers.get(question_id=1016)
        answer17 = answers.get(question_id=1017)

        self.assertEqual(answer1.text, "change")
        self.assertEqual(answer2.text, "change")
        self.assertEqual(answer3.text, "Alvin")
        self.assertEqual(answer4.text, "1")
        self.assertEqual(answer5.text, "1")
        self.assertEqual(answer6.text, "chiefinvestigator")
        self.assertEqual(answer7.text, "No")
        self.assertEqual(answer8.text, "1")
        self.assertEqual(answer9.text, "No")
        self.assertEqual(answer10.text, "1")
        self.assertEqual(answer11.text, "1")
        self.assertEqual(answer12.text, "1")
        self.assertEqual(answer13.text, "1")
        self.assertEqual(answer14.text, "1")
        self.assertEqual(answer15.text, "1")
        self.assertEqual(answer16.text, "1")
        self.assertEqual(answer17.text, "1")
        
        
        
        





