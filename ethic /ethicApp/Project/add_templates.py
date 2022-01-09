from accounts.models import Application, User, Answers, Question

# Create a user
test = User(username="exemplar", password="=g8CUu-^")
test.save()

# Create an application
app = Application(id=1, title="Exemplar", user=test,
                  supervisor="test", status="COMPLETED")
app.save()

# Add all answer objects to database using user and application data
Answers.objects.bulk_create([
    # 601 (215)
    Answers(id=1, short_answer_text="""Many participants will be first year University of Sydney psychology students who volunteer to participate by registering on the SONA system. Students will receive partial course credit in exchange for their participation in the initial part of the study. SONA participants can consent to participating in two follow-up portions of the study, one month and six months after the initial study, though they can participate in the initial study without consenting to the follow-up portions. If they consent to participating in the follow-up portions of the study one month and six months after the initial study or if they request for overall feedback for the study, university emails will be collected as a means of contact.
    We will also advertise our study on career and recruiting websites. These participants will see a description of the purpose and methodology of the study and they can choose to sign up to an appointment or will be provided with a web link where they will be provided with an information statement and opportunity to consent to participate if they choose to. Participants from the community can also consent to participating in two follow-up portions of the study, one month and six months after the initial study, though they can participate in the initial study without consenting to the follow-up portions.""", question_id=Question.objects.filter(question_num=601)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=2, short_answer_text="""Selection of participants will be on condition that they are 18 years old or over.
        Contact details will be obtained through the UoS coordinator for contacting undergraduate and postgraduate students via email. Potential participants will then be able to provide their contact details by responding to the recruitment email.""", question_id=Question.objects.filter(question_num=601)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=3, short_answer_text="""This study relates to the evaluation of software to give students feedback on their progress, so the potential participants will include students and members of the teaching team of courses who understand student feedback systems that are currently in place or the courses whose feedback is being provided.""", question_id=Question.objects.filter(question_num=601)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 602 (217)
    Answers(id=4, short_answer_text="""Potential participants will be able to see details about the study via the School of Psychology SONA system or on a careers/recruitment website advertisements for both SONA and the careers/recruitment website are attached to this application.
    There will be no pressure on the participant to take part in the study; they will be informed that their participation will be entirely voluntary with no consequences for deciding to not participate or to withdraw consent. Emails will be collected only as a means of sending follow-up questionnaires and feedback. Participants will be notified about this prior to consenting and can withdraw from the study if they do not wish to provide email details when asked.
    Participants will be given the option of participating in follow-up questionnaires one month and six months after the study. If they choose to participate in the follow-ups, they will go into a draw to win one of ten Westfield gift vouchers (valued at $25 each) following their participation in the study if they choose to provide a postal address for the voucher to be sent if they happen to win it.""", question_id=Question.objects.filter(question_num=602)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=5, short_answer_text="""We will conduct a lab experiment where interviews and observations will take place while our system is being used. An invitation email explaining the objectives of the study will be sent to: (1) undergraduate and postgraduate students of the University who are not in any student/teacher relationship with either of the researchers; (2) higher degree research students in the Faculty of Engineering and IT (via a HDR email list); (3) other University mailing lists, such as the Faculty alumni list, CHAI mailing list, etc. Potential participants will need to contact the researchers to express interest, which should avoid any form of coercion. Templates for recruiting emails are attached to this application.
    Additionally, Participant Information Statements will be distributed in units of study taught by lecturers not involved in the research project. Potential participants will need to contact the researchers or directly approach them in class to express interest, which should again avoid any form of coercion.""", question_id=Question.objects.filter(question_num=602)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=6, short_answer_text="""Students will be informed about the study during class and through online platforms used by the course coordinators. Students will identify themselves through email or online platforms that they wish to be involved.
    Other participants will be invited to participate in person, through email or social media, responding to contact through the same media. This may include past participants of subjects and past students. Both of these groups are allowed to be contacted by the university under the Spam Act (2003). The messages sent through social media and email will conform to a template attached to this application. It will also include an attachment or link to the participant information statement attached to this applicaiton.
    We may recruit participants in several groups of about 5 users, as the development and evaluation of this software will undergo an iterative design process. (see Nielsen, J., & Landauer, T. K. (1993). A mathematical model of the finding of usability problems. In Proceedings of the SIGCHI conference on Human factors in computing systems - CHI ’93 (pp. 206–213). New York, New York, USA: ACM Press. https://doi.org/10.1145/169059.169166)""", question_id=Question.objects.filter(question_num=602)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 603 (218)
    Answers(id=7, short_answer_text="""There will be no consequences of withdrawal and this fact will be noted in the Participant Information Statement.""", question_id=Question.objects.filter(question_num=603)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=8, short_answer_text="""Participants will receive a Participant Information Statement explaining that being in the study is completely voluntary: they are not under any obligation to consent and - if they do consent - they can still withdraw at any time during the execution of the study without affecting their relationship with The University of Sydney. For interviews, participants will be advised that: You may stop the interview at any time if you do not wish to continue, the audio (and/or video) recording will be erased and the information provided will not be included in the study.""", question_id=Question.objects.filter(question_num=603)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=9, short_answer_text="""There will be no consequences from withdrawing from the evaluation studies. This will be outlined in the Participant""", question_id=Question.objects.filter(question_num=603)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 605 (221)
    Answers(id=10, short_answer_text="""Participants recruited from the first year psychology student population using the SONA system will be rewarded course credit for their participation and this will be proportional to the time it takes to complete the initial study. Furthermore, both participants from SONA and the general community will receive overall feedback and specific feedback related to their phishing detection task performance. As a result, participants may be able to more accurately detect phishing content after the study, thereby improving their online security.
    Furthermore, participants who consent to participating in the one month and six month follow-up questionnaires will go into a draw to win a Westfield gift vouchers following their participation in the study if they choose to provide a postal address for the voucher to be sent if they happen to win it. Providing an address will be completely voluntary and they will be informed that their address will not be recorded separately to their other data. There are a total of 10 Westfield gift vouchers, valued at $25 each.
    For participants who are eligible for the draw, they will be asked whether or not they are willing to provide their postal addresses in the participant consent form, following consenting to the study.""", question_id=Question.objects.filter(question_num=605)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=11, short_answer_text="""Lab study participants will be offered chocolates to the amount of approximately $5.00 as a small mark of appreciation for""", question_id=Question.objects.filter(question_num=605)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=12, short_answer_text="""""", question_id=Question.objects.filter(question_num=605)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 607 (222)
    Answers(id=16, short_answer_text="""Participants will be provided the participant consent form online, in the same format shown in the attached document. At the bottom of this form, participants will be required to type in their name, the date,
    select that they do or do not consent to participating in this experiment, and select whether they wish for feedback regarding the overall results of the study.
    Participants will also be required to select whether they wish to participate in follow-up questionnaires one month and six months after the initial study. For participants who have indicated that they wish to participate in follow-up questionnaires, they will be asked whether or not they wish to type in an email address (needed to send them the follow up questionnaires and only required if they have either consented to participate to the follow-up questionnaires and/or have requested for overall feedback regarding the study). They will also be asked whether or not they wish to type in a postal address, to be sent if they win a Westfield gift voucher (participants will be told that this is not required for participation in the study, and will only be necessary to be in the draw).""", question_id=Question.objects.filter(question_num=607)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=17, short_answer_text="""All participants will be required to give their written consent before participating in the study. We will use written, as it is easier to check at a later stage if necessary we are able to store this with other materials from the study. Participants will sign the consent form which will be witnessed by the researcher.
    Participants will also be given a physical paper copy of an information statement which contains more information about the study.""", question_id=Question.objects.filter(question_num=607)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=18, short_answer_text="""All participants undertaking the evaluations studies will be asked to accept a digital participant consent form (attached to this application) after being provided with a participant information statement at the start of the evaluation test. Providing another PIS at this stage will also give the best opportunity for the user to provide informed consent, and address concerns with the researcher conducting the experiment. We believe that this method of obtaining consent is appropriate for the risk and complexity of this research.""", question_id=Question.objects.filter(question_num=607)[0], application_id=app, is_short_answer=1,
            section_name="D", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 703 (236)
    Answers(id=19, short_answer_text="""All measures are completed as online surveys which are hosted on Qualtrics. Qualtrics data is stored with the utmost security (inline with approval in Nov, 2012) and is only accessible to researchers on this project.""", question_id=Question.objects.filter(question_num=703)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=20, short_answer_text="""Audio recordings Film/Video recordings/Other""", question_id=Question.objects.filter(question_num=703)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=21, short_answer_text="""We will use the concurrent Think-Aloud research method, which includes Film/Video recording in order to record the users monologue and the screen as they use the digital system. The Think-Aloud method is a standard activity in HCI research for the evaluation of digital platforms, such as the information dashboard that we are building (See [1] and [2]).
    This Think-Aloud protocol asks the user to verbally express their internal monologue as they interact with the digital interface. This is an appropriate method for testing because the dashboard will not require a high cognitive load and will not be measuring performance metrics based on time (See [1]).
    Surveys will also be used to help the user express their level of satisfaction with the interface. There will be two short surveys to complete, each attached to this application. The first survey is the After Scenario Questionnaire [3], a three- question survey which is to be completed at the end of each task. The second survey is the System Usability Scale (SUS) [4], a very widely used metric in user experience testing.
    As well as this, the researcher will take observational notes. This is to record somatic responses that are not consciously evaluated and expressed by the user, as well as information about how effectively the system we are building supports the completion of the tasks given to participants. Data from the surveys will be stored on a secure server.
    References:
    [1] Charters, E. (2003). The Use of Think-aloud Methods in Qualitative Research An Introduction to Think-aloud Methods. Brock Education Journal, 12(2), 68–82.
    [2] van den Haak, M., De Jong, M., & Jan Schellens, P. (2003). Retrospective vs. concurrent think-aloud protocols: Testing the usability of an online library catalogue. Behaviour & Information Technology, 22(5), 339–351. https://doi.org/10.1080 /0044929031000
    [3] Lewis, J. R. (1991). Psychometric Evaluation of an After-Scenario Questionnaire for Computer Usability Studies: the ASQ. SIGCHI Bulletin, 23(I), 78–81. https://doi.org/10.1145/122672.122692
    [4] Brooke, J. (1996). SUS: A “quick and dirty” usability scale. In P. Jordan, B. Thomas, & B. Weerdmeester (Eds.), Usability Evaluation in Industry (pp. 189–194). London, UK: Taylor & Francis.""", question_id=Question.objects.filter(question_num=703)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 707 (337)
    Answers(id=22, short_answer_text="""We will be administering a mental ability (intelligence) test to participants. This test may provide insight into participants intellectual abilities. However, participants scores will only be compared against other participants in the study, not the norms. Therefore, providing participants with feedback on their performance relative to other participants on these tests are likely to be uninformative at best and probably misleading. For example, participants who do relatively poorly on the mental ability measures in comparison to other participants in this study may do relatively better in comparison to the norms.""", question_id=Question.objects.filter(question_num=707)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=23, short_answer_text="""Audio recordings will be used to record interactions and to collect feedback from recruited participants about their experience while interacting with the system.
    Video recordings will be used to collect data about the behaviour, spatial positioning, and movement of recruited participants while interacting with the system.
    The system itself will automatically collect statistical information about user interactions, such as the number of times specific features of the system are accessed. This logging information will not include any personally identifiable information.
    Recorded data will be later subject to analysis to assess participantsâ€TM responses to the system and to identify sequential patterns of behaviour during the interaction.
    We will separately seek permission for use of the videos in reports of the work and presentations.""", question_id=Question.objects.filter(question_num=707)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=24, short_answer_text="""""", question_id=Question.objects.filter(question_num=707)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 709 (342)
    Answers(id=25, short_answer_text="""Not Applicable""", question_id=Question.objects.filter(question_num=709)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=26, short_answer_text="""""", question_id=Question.objects.filter(question_num=709)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=27, short_answer_text="""""", question_id=Question.objects.filter(question_num=709)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 712 (344)
    Answers(id=28, short_answer_text="""Journal/Book publications, conference/symposia presentations""", question_id=Question.objects.filter(question_num=712)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=29, short_answer_text="""We plan to report the results of the study in a series of publications (e.g. conference papers, journal articles) as well as being presented at conferences and symposia. The results will also be used in the student researchers masters thesis.""", question_id=Question.objects.filter(question_num=712)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=30, short_answer_text="""The goal is to disseminate the results to the Faculty of Engineering and IT through a guidebook for teachers that includes examples of how data from assessments and activities can predict student outcomes and inform the educational design of subjects. The knowledge generated will also be implicitly communicated through the software we will create, that displays information dashboards for students and teachers.
        Also, we will publish our processes, findings and evaluations in journal articles and conference presentations in leading venues in the fields of Human-Computer Interaction, Learning Analytics, and Artificial Intelligence in Education.""", question_id=Question.objects.filter(question_num=712)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 714 (349)
    Answers(id=31, short_answer_text="""Research results will always be disseminated in an aggregated fashion. No individuals score will ever be specified or linked to an identifiable score. They will always be reported as group levels or means or as anonymous responses.""", question_id=Question.objects.filter(question_num=714)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=32, short_answer_text="""The participants will not be personally identifiable in the research results. Demographic information - such as gender, age, professional occupation, etc. - may be disclosed upon consent from participants but only insofar they contribute for statistical analysis of the experiment and without allowing the identification of the participants in question. Video and still images of the participants will only be included in the disseminated material if faces are blurred enough to prevent personal identification and if the participants have agreed to this use of the video.""", question_id=Question.objects.filter(question_num=714)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=33, short_answer_text="""Reporting on the results of the evaluations will have participants personally identifiable information removed, with participants referred to using a key, such as Participant 1, or P1 etc. Where appropriate, quantitative data will be aggregated.""", question_id=Question.objects.filter(question_num=714)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 716 (352)
    Answers(id=34, short_answer_text="""Depending on the journal to which we submit results for publication, we may be required to deposit the data into a public repository for other researchers to examine. In such cases, all identifiable and potentially reidentifiable information about participants will be removed. These cases will be made clear under section 9 of the Participant Information Statement. They read as follows: We will keep the information we collect for this study, and we may use it in future projects. By providing your consent you are allowing us to use your information in future projects. We dont know at this stage what these other projects will involve. We will seek ethical approval before using the information in these future projects.
    We may submit the information from this project to a public database for research information, so that other researchers can access it and use it in their projects. Before we do so, we will take out all the identifying information so that the people we give it to wont know whose information it is. They wont know that you participated in the project and they wont be able to link you to any of the information you provided.""", question_id=Question.objects.filter(question_num=716)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=35, short_answer_text="""""", question_id=Question.objects.filter(question_num=716)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=36, short_answer_text="""""", question_id=Question.objects.filter(question_num=716)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 717 (351)
    Answers(id=37, short_answer_text="""Participants will be able to request a one-page lay summary of the results when filling in the consent form. Prior to indicating their consent, they can select whether or not they would like to receive feedback about the overall results of this study via email. If participants have indicated that they would like to receive feedback regarding the overall study results, they will be prompted to type in their contact email. Once all collection has ended and the results have been prepared, we will email those participants who elect to receive feedback a one-page lay summary of the results. In addition to the option in the Consent Form, the option to receive this feedback will also be communicated under question 12 of the Participant Information Statement (see attached PIS_SONA_CyberStudy.pdf and PIS_General_CyberStudy.pdf ).""", question_id=Question.objects.filter(question_num=717)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=38, short_answer_text="""Participants who request feedback will be emailed a copy of the final compiled results for the study.""", question_id=Question.objects.filter(question_num=717)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=39, short_answer_text="""An email summary can be produced in February 2018 (at the end of the funding from this research project) to participants who accept to being contacted about the results of this study in the Participant Consent Form.""", question_id=Question.objects.filter(question_num=717)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 718 (353)
    Answers(id=40, short_answer_text="""All study material will be administered using the online survey engine, Qualtrics. All data will therefore be stored in the Qualtrics secure database (approved for use by the HREC executive in November, 2012).""", question_id=Question.objects.filter(question_num=718)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=41, short_answer_text="""As we reported initially, we ensure the data is stored at the Student Administration Centre in 2E-Reception, Level 2, J12 SIT Building, Cnr Cleveland St and City Rd, The University of Sydney, NSW 2006.
    Physical documents will be scanned and stored digitally with the rest of the digital recordings. It will all be password protected. The password will be stored in the Student Administration Centre as well.
    During the study, the material will be kept on the researcher’s secure password protected computer where only the researchers involved in this project have access.
    Upon completion of the project, the study materials will be stored on a USB storage device that will be locked securely in Student Administration, Level 2, J12 SIT Building, Cnr Cleveland St and City Rd, The University of Sydney, NSW 2006. Physical documents will be scanned and stored digitally with the rest of the digital recordings. It will all be password protected.
    Chief Investigator/Supervisor:
    Digital copies will be stored in the Chief Investigator office on a password-protected computer, in Room 3W-307, J12 SIT Building, Cnr Cleveland St and City Rd, The University of Sydney, NSW 2006.""", question_id=Question.objects.filter(question_num=718)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=42, short_answer_text="""The data from evaluations will also be held on secure servers, including Videos, Participant Consent Forms, Surveys and""", question_id=Question.objects.filter(question_num=718)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 719 (354)
    Answers(id=43, short_answer_text="""Study materials will be stored electronically only. These electronic materials will be stored in Qualtrics and password""", question_id=Question.objects.filter(question_num=719)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=44, short_answer_text="""The data will be stored at the Student Administration Centre in 2E-Reception, Level 2, J12 SIT Building, Cnr Cleveland St and City Rd, The University of Sydney, NSW 2006. Physical documents will be scanned and stored digitally with the rest of the digital recordings. It will all be password protected. The password will be stored in the Student Administration Centre as well.""", question_id=Question.objects.filter(question_num=719)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=45, short_answer_text="""The data from evaluations will also be held on secure servers, including Videos, Participant Consent Forms, Surveys and""", question_id=Question.objects.filter(question_num=719)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 720 (355)
    Answers(id=46, short_answer_text="""Qualtrics data is stored with the utmost security (in line with approval in Nov, 2012) and is only accessible to researchers on this project. When data is downloaded from Qualtrics to the researchers private computers for analysis, the only information related to the identity of the participant will be a random alpha-numeric code generated by Qualtrics. These random codes can only be matched to student names stored in relation to the Participant Consent Form by accessing the researchers password protected Qualtrics accounts. Other than the consent form information, participants will only be linked by these random codes.""", question_id=Question.objects.filter(question_num=720)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=47, short_answer_text="""During the study, the material will be kept on the researchers secure password protected computer where only the researchers involved in this project have access.
    Upon completion of the project, the study materials will be stored on an USB storage device that will be locked securely in Student Administration, Level 2, J12 SIT Building, Cnr Cleveland St and City Rd, The University of Sydney, NSW 2006. Physical documents will be scanned and stored digitally with the rest of the digital recordings. It will all be password protected.""", question_id=Question.objects.filter(question_num=720)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=48, short_answer_text="""The server we use to store data from our evaluation testing will be on a secure server, where access is restricted to the research team.
    Data we collect will be de-identified using a key (participant 1 etc), except for Participant Consent Forms. Video recordings will be of the screen and the users interactions, rather than of the user.""", question_id=Question.objects.filter(question_num=720)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 723 (357)
    Answers(id=52, short_answer_text="""If the study is submitted into a journal that requests for the data to be submitted, study materials will be retained in perpetuity. Otherwise, the digital files will be deleted from computer hard drives and Qualtrics after 5 years as there is no requirement to keep this data for a longer period of time.""", question_id=Question.objects.filter(question_num=723)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=53, short_answer_text="""The data will be deleted after a maximum of 5 years to comply with state regulations. This amount of time is suitable as""", question_id=Question.objects.filter(question_num=723)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=54, short_answer_text="""The data we collect for evaluation will be archived after the research funding has ended in February, and stored in""", question_id=Question.objects.filter(question_num=723)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 724 (359)
    Answers(id=55, short_answer_text="""Project Materials will be kept in perpetuity if the study is submitted into a journal that requests for the data to be submitted. Otherwise, the digital files will be deleted from computer hard drives and Qualtrics after 5 years.""", question_id=Question.objects.filter(question_num=724)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=56, short_answer_text="""Any hard paper copies will be securely shredded and disposed of. All digital data will be erased.""", question_id=Question.objects.filter(question_num=724)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=57, short_answer_text="""N/A""", question_id=Question.objects.filter(question_num=724)[0], application_id=app, is_short_answer=1,
            section_name="E", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 801 (361)
    Answers(id=58, short_answer_text="""No foreseeable risk of harm""", question_id=Question.objects.filter(question_num=801)[0], application_id=app, is_short_answer=1,
            section_name="F", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=59, short_answer_text="""N/A.""", question_id=Question.objects.filter(question_num=801)[0], application_id=app, is_short_answer=1,
            section_name="F", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=60, short_answer_text="""There is no perceived risk of discomfort or harm to participants involved with the dashboard evaluations. Dashboard evaluations will take place in an office-like environment, and poses no risk to physical harm based on this testing.""", question_id=Question.objects.filter(question_num=801)[0], application_id=app, is_short_answer=1,
            section_name="F", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

    # 802 (362)
    Answers(id=61, short_answer_text="""None""", question_id=Question.objects.filter(question_num=802)[0], application_id=app, is_short_answer=1,
            section_name="F", is_referenced=1, is_exemplar=0, answer_type="crowedsource"),
    Answers(id=62, short_answer_text="""It is well documented that even with careful design of the interface there is potential for participants to experience motion sickness while wearing the head mounted display to explore virtual worlds. Not everyone experiences this. We will warn participants of this possibility in the initial briefing. We will explain that if it does happen participants can sit down and quit the study. We will invite participants to trial the device briefly at that time to assess how they find it.""", question_id=Question.objects.filter(question_num=802)[0], application_id=app, is_short_answer=1,
            section_name="F", is_referenced=1, is_exemplar=0, answer_type="labstudy"),
    Answers(id=63, short_answer_text="""There are no perceived risks to the research team.""", question_id=Question.objects.filter(question_num=802)[0], application_id=app, is_short_answer=1,
            section_name="F", is_referenced=1, is_exemplar=0, answer_type="thinkaloud"),

])
