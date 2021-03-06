from django.test import TestCase, RequestFactory
from django.test import Client
from accounts.forms import CreateUserForm
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.models import Group
from django.contrib.sessions.middleware import SessionMiddleware
from accounts.models import Application, Question, Answers, CoverSheetQuestion
from qualifier.views import success
from .views import questionnaire


# class AccountsTest(TestCase):

#     @classmethod
#     def setUpTestData(cls):

#         researcher = Group(name = "researcher")
#         staff = Group(name = "staff")
#         staff.save()
#         researcher.save()
#         cls.user = User.objects.create_user(username = 'john', password='johnpassword')
#         cls.admin_staff = User.objects.create_user(username='admin', password='adminpassword')
#         cls.admin_staff.groups.add(staff)
#         cls.user.groups.add(researcher)
#         cls.factory = RequestFactory()

#         CoverSheetQuestion.objects.bulk_create([

#             CoverSheetQuestion(question_num=1001, text = 'Provide a lay summary of the project:', is_short_answer=1),
#             CoverSheetQuestion(question_num=1002, text = 'Protocol Title:', is_short_answer=1),
#             CoverSheetQuestion(question_num=1003, text = 'First Named Chief Investigator Name:', is_short_answer=1),
#             CoverSheetQuestion(question_num=1004, text = 'First Named Chief Investigator ID:', is_short_answer=1),
#             CoverSheetQuestion(question_num=1005, text = 'School/Centre', is_short_answer=0),
#             CoverSheetQuestion(question_num=1006, text = 'Role', is_short_answer=1),
#             CoverSheetQuestion(question_num=1007, text = 'Other Internal Investigators Involved:', is_short_answer=0),
#             CoverSheetQuestion(question_num=1008, text = 'Number of Internal Investigators (including Chief Investigator):', is_short_answer=0),
#             CoverSheetQuestion(question_num=1009, text = 'Other External Investigators Involved:', is_short_answer=0),
#             CoverSheetQuestion(question_num=1010, text = 'Number of External Investigators:', is_short_answer=0),
#             CoverSheetQuestion(question_num=1011, text = 'Responsible:', is_short_answer=1),
#             CoverSheetQuestion(question_num=1012, text = 'Current State:', is_short_answer=1),
#             CoverSheetQuestion(question_num=1013, text = 'HREC name:', is_short_answer=1),
#             CoverSheetQuestion(question_num=1014, text = 'Action:', is_short_answer=1),
#             CoverSheetQuestion(question_num=1015, text = 'Title:', is_short_answer=1),
#             CoverSheetQuestion(question_num=1016, text = 'Action:', is_short_answer=1),
#             CoverSheetQuestion(question_num=1017, text = 'Please provide any other relevant details:', is_short_answer=1),
#         ])
        

#         Question.objects.bulk_create([
#             Question(question_num=101, text = 'Is this project a University of Sydney student project ONLY ?', is_short_answer=0, section_name='A',tips = 'Tips: i.e. ethics application restricted to the activities of the student research project', is_qualifier_question = 0),
#             Question(question_num=102, text = 'Select appropriate student classification:', is_short_answer=2, section_name='A',tips = 'Tips: ', is_qualifier_question = 0),
#             Question(question_num=103, text = 'Indicate whether this project has been or will be submitted to any other ethics committees', is_short_answer=0, section_name='A', tips = 'Tips: ', is_qualifier_question = 0),
#             Question(question_num=201, text = 'Does your research involve women who are pregnant and the human foetus?', is_short_answer=0, section_name='B', tips = 'Tips: ', is_qualifier_question = 1),
#             Question(question_num=202, text = 'Does your study involve children and/or young people ?', is_short_answer=0, section_name='B', tips = 'Tips: i.e. younger than 18 years', is_qualifier_question = 1),
#             Question(question_num=203, text = 'Does your study involve people in existing dependent or unequal relationships with the researcher(s)?', is_short_answer=0, section_name='B', tips = 'Tips: ', is_qualifier_question = 1),
#             Question(question_num=204, text = 'Does your research involve people with a cognitive impairment, an intellectual disability or a mental illness?', is_short_answer=0, section_name='B', tips = 'Tips: ', is_qualifier_question = 1),
#             Question(question_num=205, text = 'Does your research involve people highly dependent on medical care who may be unable to give consent?', is_short_answer=0, section_name='B', tips = 'Tips: ', is_qualifier_question = 1),
#             Question(question_num=206, text = 'Does your study have the potential to discover illegal activity by participants or others? This includes research intending to expose illegal activity, as well as research not specifically designed to, but likely to discover, illegal activity.', is_short_answer=0, section_name='B', tips = 'Tips: ', is_qualifier_question = 1),
#             Question(question_num=207, text = 'Does your research involve Aboriginal and/or Torres Strait Islander peoples?', is_short_answer=0, section_name='B', tips = 'Tips: ', is_qualifier_question = 1),
#             Question(question_num=208, text = 'Does your research involve CALD people?', is_short_answer=0, section_name='B', tips = 'Tips: CALD (Culturally and Linguistically Diverse)', is_qualifier_question = 1),
#             Question(question_num=209, text = 'Does your research involve travel overseas?', is_short_answer=0, section_name='B', tips = 'Tips: ', is_qualifier_question = 1),
#             Question(question_num=210, text = 'Is your study likely to cause or elicit distress in participants due to its subject matter, the procedures involved, information that might be revealed about the participant or related persons, or in some other way?', is_short_answer=0, section_name='B', tips = 'Tips: ', is_qualifier_question = 1),
#             Question(question_num=211, text = 'Does your study involve research that could jeopardise a participant\'s employment?', is_short_answer=0, section_name='B',tips = 'Tips: ', is_qualifier_question = 1),
#             Question(question_num=212, text = 'Is your proposed research a clinical trial? A clinical trial is a form of research designed to find out the effects of an intervention, including a treatment or diagnostic procedure. A clinical trial can involve testing a drug, a surgical procedure, other therapeutic procedures and devices, a preventive procedure, or a diagnostic device or procedure.', is_short_answer=0, section_name='B', tips = 'Tips: ',is_qualifier_question = 1),
#             Question(question_num=213, text = 'Does your study involve the use of human tissue?', is_short_answer=0, section_name='B', tips = 'Tips: ', is_qualifier_question = 1),
#             Question(question_num=214, text = 'Does your study involve human genetics or human stem cells?', is_short_answer=0, section_name='B',tips = 'Tips: ', is_qualifier_question = 1),
#             Question(question_num=215, text = 'Does your study involve research that poses a risk to the physical or emotional safety or welfare of a University of Sydney student researcher? If you are a student and your research takes place off-campus a completion of a safety protocol may be necessary.', is_short_answer=0, section_name='B',tips = 'Tips: e.g. honours student or postgraduate student', is_qualifier_question = 1),
#             Question(question_num=216, text = 'Does your research involve any of the following: Collection of biological samples (e.g. blood, saliva, bodily fluids). Physical screening (e.g. blood pressure, cholesterol, physical fitness, MRI scans). Physical exertion? (i.e. physical activity, exercise).', is_short_answer=0, section_name='B', tips = 'Tips: ', is_qualifier_question = 1),
#             Question(question_num=217, text = 'Does the research ONLY involve existing collections of data or records about human beings ?', is_short_answer=0, section_name='B', tips = 'Tips: collected with appropriate ethical approval', is_qualifier_question = 1),
#             Question(question_num=218, text = 'Is there a foreseeable risk of more than \'discomfort\'? For a useful description of the differences betweenharm, discomfort and inconvenience please refer to the National Statement on Ethical Conduct in Human Research, Chapter 2.1', is_short_answer=0, section_name='B', tips = 'Tips: ', is_qualifier_question = 1),
#             Question(question_num=219, text = 'How will the process of obtaining consent avoid perceived/actual coercion and enable persons in dependent relationships to give voluntary consent?', is_short_answer=1, section_name='B', tips = 'Tips: ', is_qualifier_question = 1),
            
#             Question(question_num=501, text = 'Are any "conflict of interest" issues likely to arise in relation to this research?', is_short_answer=0, section_name='C', tips = 'Tips: ', is_qualifier_question = 0),
#             Question(question_num=502, text = 'Do the researchers have any affiliation with, or financial involvement in, any organisation or entity with direct or indirect interests in the subject matter or materials of this research? ', is_short_answer=0, section_name='C', tips = 'Tips: Note that such benefits must be declared in the Participant Information Statement', is_qualifier_question = 0),
#             Question(question_num=503, text = 'Do the researchers expect to obtain any direct or indirect financial or other benefits from conducting this research? ', is_short_answer=0, section_name='C', tips = 'Tips: Note that such benefits must be declared in the Participant Information Statement', is_qualifier_question = 0),
#             Question(question_num=504, text = 'Have conditions already been imposed OR are likely to be imposed in the future, upon the use (e.g. publication), or ownership of the results (e.g. scientific presentations) or materials (e.g. audio-recordings), by any party other than the listed researchers?', is_short_answer=0, section_name='C', tips = 'Tips: ', is_qualifier_question = 0),

#             Question(question_num=601, text = 'Describe how you will identify and select potential participants for recruitment into the study. You should include information about how you will obtain contact details for potential particpants.', is_short_answer=1, section_name='D', tips = 'Tips: ', is_qualifier_question = 0),
#             Question(question_num=602, text = 'Describe how and where initial contact will be made with potential participants and how you will avoid real or perceived coercion. Copies of all relevant correspondence (e.g) email, letter of introduction, covering letter, circular/flyer etc.) need to be uploaded with your application. If you are using email addresses please outline how their use will not be in breach of privacy or spam legislation.', is_short_answer=1, section_name='D',tips = 'Tips: ', is_qualifier_question = 0),
#             Question(question_num=603, text = 'If a participant, or person on behalf of a participant, chooses to withdraw from the research, what specific consequences should they be made aware of, prior to giving consent?', is_short_answer=1, section_name='D', tips = 'Tips: These details should be included in the Participant Information Statement.', is_qualifier_question = 0),
#             Question(question_num=604, text = 'Will participants receive any reimbursement of out-of-pocket expenses, or financial or other "rewards" as a result of participation?', is_short_answer=0, section_name='D', tips = 'Tips: ', is_qualifier_question = 0),
#             Question(question_num=605, text = 'Specify the nature and value of any proposed incentive/payment (e.g. movie tickets, food vouchers) or reimbursement (e.g. travel expenses) to participants. Explain why this offer will not impair the voluntary nature of the consent, whether by participants or persons deciding for their behalf. Payment that is disproportionate to the time involved, or any other inducement that is likely to encourage participants to take risks, is ethically unacceptable. (See 2.2.10 and 2.2.11 of the National Statement). Note that monetary amounts should not be specified in advertisements, but payments should be disclosed in the Participant Information Statement in accordance with 2.2.6(j) of the National Statement. ', is_short_answer=1, section_name='D',tips = 'Tips: ', is_qualifier_question = 0),
#             Question(question_num=606, text = 'How will consent be obtained?', is_short_answer=1, section_name='D', tips = 'Tips: ', is_qualifier_question = 0),
#             Question(question_num=607, text = 'Please clarify your response to the question above and justify with reference to the National Statement. For instance, if you indicated that consent will be written and oral, does the refer to all participants undergoing written and oral consent or does it refer the different consent processes for different participant groups? You should justify why you have chosen these forms of consent. If you are using oral consent, explain how it will be recorded (e.g. In field notes, using tape recording).', is_short_answer=1, section_name='D',tips = 'Tips: e.g section 2.2.5, 3.1.16, 5.2.16', is_qualifier_question = 0),
#             Question(question_num=608, text = 'Will there be participants who are not fluent in English or who have difficulty understanding English? ', is_short_answer=0, section_name='D', tips = 'Tips: ', is_qualifier_question = 0),
#             Question(question_num=609, text = 'Is there an intention to recruit participants who have physical impairment or disability that may affect the consent process ?', is_short_answer=1, section_name='D',tips = 'Tips: e.g. blind/vision/deaf/hearing impaired/speech impaired',is_qualifier_question = 0),

#             Question(question_num=701, text = 'Will any part of the project involve recordings ?', is_short_answer=0, section_name='E', tips = 'Tips: e.g. audio, video, online surveys', is_qualifier_question = 0),
#             Question(question_num=702, text = 'Which of the following recordings will be used in the project? More than one may apply.', is_short_answer=2, section_name='E', tips = 'Tips: ', is_qualifier_question = 0),
#             Question(question_num=703, text = 'Outline how these recordings will be used and why they are necessary to achieve the aims of the research project. If your project involves online surveys, state where the surveys will be hosted and comment on any security, data ownership and privacy constraints associated with this survey host.', is_short_answer=1, section_name='E', tips = 'Tips: ',is_qualifier_question = 0),
#             Question(question_num=704, text = 'The following questions will establish whether the HREC needs to apply federal or state/territory privacy legislation when reviewing your ethics application. Will you use, collect or disclose information about human participants from an agency, authority or organisation? This includes Commonwealth agencies, private sector organisations, state/territory agencies and international organisations. For instance, you may be using information from a medical practice, a hospital, a university, a state or federal government department. You should say yes even if it is your own organisation ', is_short_answer=0, section_name='E',tips = 'Tips: e.g. your medical practice',is_qualifier_question = 0),
#             Question(question_num=705, text = 'Is the research project likely to produce information or results that are of personal significance to individual participants? For instance, a project may reveal that participants are at risk of developing a particular disease, provide insight into their intellectual/other abilities, or indicate that they have physical or mental health problems.', is_short_answer=0, section_name='E', tips = 'Tips: ',is_qualifier_question = 0),
#             Question(question_num=706, text = 'Is it intended that any such information that is of potential significance to participants will be reported back to the individual concerned?', is_short_answer=0, section_name='E', tips = 'Tips: ',is_qualifier_question = 0),
#             Question(question_num=707, text = 'Explain why these results will not be reported back to individual participants', is_short_answer=1, section_name='E',tips = 'Tips: ',is_qualifier_question = 0),
#             Question(question_num=708, text = 'Will the participant be told that their results will be reported to this third party?', is_short_answer=0, section_name='E',tips = 'Tips: ',is_qualifier_question = 0),
#             Question(question_num=709, text = 'Explain why the participant will not be told that their results will be reported to this third party.', is_short_answer=1, section_name='E',tips = 'Tips: ',is_qualifier_question = 0),
#             Question(question_num=710, text = 'Is the research project likely to reveal a significant risk to the health or wellbeing of persons other than the participant?', is_short_answer=0, section_name='E',tips = 'Tips: e.g. family members, colleagues, community members',is_qualifier_question = 0),
#             Question(question_num=711, text = 'Does this project involve the use of information that you or your organisation had collected previously for another purpose?', is_short_answer=0, section_name='E',tips = 'Tips: ',is_qualifier_question = 0),
#             Question(question_num=712, text = 'Describe how the overall results of this research project will be disseminated .', is_short_answer=1, section_name='E',tips = 'Tips: e.g. journal publications and book chapters, conference presentations, student theses, creative works',is_qualifier_question = 0),
#             Question(question_num=713, text = 'Will the confidentiality of participants and privacy of their data be protected in the dissemination of overall research results? Please note that if you propose to identify individuals in publications, you should select no?? here and obtain their consent for this. Please also note that if you have obtained personal information without individual consent under a waiver of consent, you can only publish this information in de-identified form.', is_short_answer=0, section_name='E',tips = 'Tips: ',is_qualifier_question = 0),
#             Question(question_num=714, text = 'Explain how confidentiality of participants and privacy of their data will be protected in the dissemination of research results.', is_short_answer=1, section_name='E',tips = 'Tips: ',is_qualifier_question = 0),
#             Question(question_num=715, text = 'Will the information generated in this research project be used for any purpose(s) other than those outlined in this application? For example, will data be retained and used in future research projects, used to establish a database/research register, provided to a third party or to a public data sharing resource? Please note that this question does not refer to the use of the data for the purposes of this project .', is_short_answer=0, section_name='E',tips = 'Tips: e.g. publication of results',is_qualifier_question = 0),
#             Question(question_num=716, text = 'You have indicated that the information generated in this research project will or may be used foranother purpose. Please describe this other purpose here and ensure it is outlined on the Participant Information Statement/Consent Form. If this other purpose involves data being made available to other researchers or third parties, outline the standards that will be applied to protect participants privacy and the confidentiality of data. Please note that ethical approval will also need to be sought in future for any secondary use of the data', is_short_answer=1, section_name='E',tips = 'Tips: ', is_qualifier_question = 0),
#             Question(question_num=717, text = 'Outline how feedback concerning the overall results of the project will be made available to participants (e.g. via a lay summary or newsletter). If participants are not to receive feedback, please justify why not.', is_short_answer=1, section_name='E',tips = 'Tips: ',is_qualifier_question = 0),
#             Question(question_num=718, text = 'Describe where study materials will be stored DURING the project (including electronic and hard copy files, consent forms, audio recordings, questionnaires, interview transcripts, video recordings, photographs etc). Please include building and room numbers for hard copy materials.', is_short_answer=1, section_name='E',tips = 'Tips: ',is_qualifier_question = 0),
#             Question(question_num=719, text = 'Describe where study materials will be stored upon COMPLETION of the project (including electronic and hardcopy files, consent forms, audio recordings, questionnaires, interview transcripts, video recordings, photographs etc). Please include building and room numbers for hardcopy materials. Note that on conclusion of the project a copy of all materials must be kept in an accessible and secure location on University premises.', is_short_answer=1, section_name='E',tips = 'Tips: ',is_qualifier_question = 0),
#             Question(question_num=720, text = 'Outline the security measures that will be used to protect study materials from misuse, loss or unauthorised access during and after the project .', is_short_answer=1, section_name='E',tips = 'Tips: e.g. removal of identifiers, secure storage, restriction of access to appropriate personnel etc',is_qualifier_question = 0),
#             Question(question_num=721, text = 'Specify how long study materials will be retained for after project completion. Please note that the options provided below are intended to facilitate compliance with relevant legislation from the State Records Authority of NSW. Data from research involving children; and from clinical trials, scanning and radioactivity studies, clinical studies, genetic manipulation, human tissue studies, and psychological research that has potential long term effects must be retained for a minimum of 20 years or until participants are 25 years of age (whichever is longer). Data from other types of studies must be retained for a minimum of 5 years. For some types of research (e.g. oral history, gene therapy) or where it is intended to reuse data in the future, it is appropriate to retain data in perpetuity (i.e. indefinitely)', is_short_answer=1, section_name='E',tips = 'Tips: ',is_qualifier_question = 0),
#             Question(question_num=722, text = 'At the end of the project, will study materials/information be stored in individually identifiable or re-identifiable form? Please note that this does not refer to the consent forms. Individually identifiable information is that from which the identity of a specific individual can reasonably be ascertained. Re-identifiable information has had identifiers removed and replaced by a code, so it is possible to identify individuals by using the code. Non-identifiable information has had all identifiers irreversibly removed or was never identifiable .', is_short_answer=0, section_name='E',tips = 'Tips: see Chapter 3.2 of the National Statement for more information',is_qualifier_question = 0),
#             Question(question_num=723, text = 'Explain why this storage period has been chosen.', is_short_answer=1, section_name='E',tips = 'Tips: ',is_qualifier_question = 0),
#             Question(question_num=724, text = 'If they are not to be kept in perpetuity, how will project materials ultimately be disposed of?', is_short_answer=1, section_name='E',tips = 'Tips: ',is_qualifier_question = 0),

#             Question(question_num=801, text = 'Participation in research can involve potential harm to participants including physical, psychological, reputational, financial, spiritual, emotional and social distress. Please outline any potential harm and justify it with regard to the potential benefits of the project. What steps will the researchers take to minimise potential harm endured as a consequence of participation?', is_short_answer=1, section_name='F',tips = 'Tips: e.g. by providing access/information to counselling',is_qualifier_question = 0),
#             Question(question_num=802, text = 'Are there any other risks involved in this research? For example, to the research team, the organisation, others? What are these risks? Explain how these risks will be negated/ minimised/ managed.', is_short_answer=1, section_name='F',tips = 'Tips: ',is_qualifier_question = 0),

#             Question(question_num=901, text = 'The nature of this project is most appropriately described as research involving :', is_short_answer=2, section_name='G',tips = 'Tips: more than one may apply',is_qualifier_question = 0),
#             Question(question_num=902, text = 'Are you doing research in a context which requires you to get permission from an appropriate authority e.g. a school, corporation, NGO, or similar?', is_short_answer=0, section_name='G',tips = 'Tips: ',is_qualifier_question = 0),
#             Question(question_num=903, text = 'Outline in lay language the theoretical, empirical and/or conceptual basis, background evidence for the research proposal with reference to the relevant literature (include at least four research citations). Note, that your study should be "based on a thorough study of the current literature, as well as previous studies" (NS 1.1 c).', is_short_answer=1, section_name='G',tips = 'Tips: ',is_qualifier_question = 0),
#             Question(question_num=904, text = 'Outline in lay language the methodology for the research proposal. Note, that you study should be "designed or developed using methods appropriate for achieving the aims of the proposal" (NS 1.1 b). Your response should include: Aims and hypotheses/research questions Research plan including duration of the study and/or timeline Participant characteristics including sex, age range and inclusion/exclusion criteria (if relevant) The intended sample size with a justification, and/or the particiant sampling/selection strategy (as relevant to your study) Details of where the study will be undertaken (location/site/URL) Details of how data will be collected and analysed Potential significance of the study', is_short_answer=1, section_name='G',tips = 'Tips: ',is_qualifier_question = 0),
#             Question(question_num=905, text = 'Thank you for completing the University of Sydney\'s Human Ethics Application Questionnaire. After selecting \'Completed\' below, please remember to attach any documents relevant to your application in the next tab. After completing your application, return to the \'Coversheet\' tab and press the \'Submit\' button. You will receive an email shortly after confirming your submission. Once again, if your require further information on the application procedure, please consult our website or email the Human Ethics team at ro.humanethics@sydney.edu.au If you experience any technical difficulties, please do not hesitate to contact Research Support using the details below: T +61 2 8627 8183 E research.support@sydney.edu.au', is_short_answer=0, section_name='G',tips = 'Tips: ',is_qualifier_question = 0),
#         ])

#     def test1(self):


#         request1 = self.factory.post('/qualifier/success')
#         request1.user = self.user
#         response1 = success(request1)


#         data = {'601': 'hello'}

#         request2 = self.factory.post('/questionnaire/1', data)
#         request2.user = self.user
#         response2 = questionnaire(request2, 1)

#         question_num = Question.objects.get(question_num = 601)
#         application_num = Application.objects.get(id=1)
        
#         result = Answers.objects.get(question_id=question_num, application_id=application_num)
#         self.assertEqual(result.short_answer_text, 'hello')










 


