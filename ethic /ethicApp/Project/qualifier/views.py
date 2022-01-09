
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.shortcuts import render, redirect
from accounts.models import Question, Answers
from accounts.models import Application
from accounts.models import CoverSheetQuestion
from accounts.models import CoverSheetAnswers
from django.http import HttpResponse
from .forms import CoverSheetForm
# Create your views here.


@login_required(login_url='login')
@allowed_users(allowed_roles=['researcher'])
def welcome(request):
    # View for qualifier/welcome page
    if request.method == 'POST':
        # If submit clicked go to qualifier/quiz
        return redirect('quiz')
    return render(request, 'welcome.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['researcher'])
def failure(request):
    # View for qualifier/failure page
    if request.method == 'POST':
        # If next clicked go back to home
        return redirect('managelist')
    return render(request, 'failure.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['researcher'])
def success(request):
    if request.method == 'POST':

        coversheet_form = CoverSheetForm(request.POST)

        if len(Application.objects.all()) == 0:
            new_id = 1
        else:
            new_id = Application.objects.latest("id").id + 1
        new_application = Application.objects.create(
            id=new_id, user=request.user, status="IN PROGRESS", supervisor="", title="")

        #summary_text = coversheet_form.cleaned_data['summary']
        csq_id_1001 = CoverSheetQuestion.objects.get(pk=1001)
        Summary = CoverSheetAnswers.objects.create(
            text="", question_id=csq_id_1001, application_id=new_application, is_short_answer=True)

        #protocol_text = coversheet_form.cleaned_data['protocol']
        csq_id_1002 = CoverSheetQuestion.objects.get(pk=1002)
        Protocol = CoverSheetAnswers.objects.create(
            text="", question_id=csq_id_1002, application_id=new_application, is_short_answer=True)

        #investigatorname_text = coversheet_form.cleaned_data['investigatorname']
        csq_id_1003 = CoverSheetQuestion.objects.get(pk=1003)
        Investigatorname = CoverSheetAnswers.objects.create(
            text="", question_id=csq_id_1003, application_id=new_application, is_short_answer=True)

        #investigatorid_text = coversheet_form.cleaned_data['investigatorid']
        csq_id_1004 = CoverSheetQuestion.objects.get(pk=1004)
        Investigatorid = CoverSheetAnswers.objects.create(
            text="", question_id=csq_id_1004, application_id=new_application, is_short_answer=True)

        #center_text = coversheet_form.cleaned_data['center']
        csq_id_1005 = CoverSheetQuestion.objects.get(pk=1005)
        Center = CoverSheetAnswers.objects.create(
            text="", question_id=csq_id_1005, application_id=new_application, is_short_answer=True)

        #role_text = coversheet_form.cleaned_data['role']
        csq_id_1006 = CoverSheetQuestion.objects.get(pk=1006)
        Role = CoverSheetAnswers.objects.create(
            text="chief investigator", question_id=csq_id_1006, application_id=new_application, is_short_answer=False)

        #otherinternalinvestigators_text = coversheet_form.cleaned_data['otherinternalinvestigators']
        csq_id_1007 = CoverSheetQuestion.objects.get(pk=1007)
        Otherinternalinvestigators = CoverSheetAnswers.objects.create(
            text="No", question_id=csq_id_1007, application_id=new_application, is_short_answer=False)

        #internalinvestigatorsnumber_text = coversheet_form.cleaned_data['internalinvestigatorsnumber']
        csq_id_1008 = CoverSheetQuestion.objects.get(pk=1008)
        Internalinvestigatorsnumber = CoverSheetAnswers.objects.create(
            text="0", question_id=csq_id_1008, application_id=new_application, is_short_answer=True)

        #otherexternalinvestigators_text = coversheet_form.cleaned_data['otherexternalinvestigators']
        csq_id_1009 = CoverSheetQuestion.objects.get(pk=1009)
        Otherexternalinvestigators = CoverSheetAnswers.objects.create(
            text="No", question_id=csq_id_1009, application_id=new_application, is_short_answer=False)

        #externalinvestigatorsnumber_text = coversheet_form.cleaned_data['externalinvestigatorsnumber']
        csq_id_1010 = CoverSheetQuestion.objects.get(pk=1010)
        Externalinvestigatorsnumber = CoverSheetAnswers.objects.create(
            text="0", question_id=csq_id_1010, application_id=new_application, is_short_answer=True)

        #responsible_text = coversheet_form.cleaned_data['responsible']
        csq_id_1011 = CoverSheetQuestion.objects.get(pk=1011)
        Responsible = CoverSheetAnswers.objects.create(
            text="", question_id=csq_id_1011, application_id=new_application, is_short_answer=True)

        #currentstate_text = coversheet_form.cleaned_data['currentstate']
        csq_id_1012 = CoverSheetQuestion.objects.get(pk=1012)
        Currentstate = CoverSheetAnswers.objects.create(
            text="", question_id=csq_id_1012, application_id=new_application, is_short_answer=True)

        #HRECname_text = coversheet_form.cleaned_data['HRECname']
        csq_id_1013 = CoverSheetQuestion.objects.get(pk=1013)
        hRECname = CoverSheetAnswers.objects.create(
            text="", question_id=csq_id_1013, application_id=new_application, is_short_answer=True)

        #action_text = coversheet_form.cleaned_data['action']
        csq_id_1014 = CoverSheetQuestion.objects.get(pk=1014)
        Action = CoverSheetAnswers.objects.create(
            text="", question_id=csq_id_1014, application_id=new_application, is_short_answer=True)
        # Action.save()

        #title_text = coversheet_form.cleaned_data['title']
        csq_id_1015 = CoverSheetQuestion.objects.get(pk=1015)
        Title = CoverSheetAnswers.objects.create(
            text="", question_id=csq_id_1015, application_id=new_application, is_short_answer=True)
        # Title.save()

        #contractaction_text = coversheet_form.cleaned_data['contractaction']
        csq_id_1016 = CoverSheetQuestion.objects.get(pk=1016)
        Contractaction = CoverSheetAnswers.objects.create(
            text="", question_id=csq_id_1016, application_id=new_application, is_short_answer=True)

        #otherrelevantdetails_text = coversheet_form.cleaned_data['otherrelevantdetails']
        csq_id_1017 = CoverSheetQuestion.objects.get(pk=1017)
        Otherrelevantdetails = CoverSheetAnswers.objects.create(
            text="", question_id=csq_id_1017, application_id=new_application, is_short_answer=True)

        questions = Question.objects.all()
        for i in questions:
            new_answer_obj = Answers.objects.create(question_id=i,
                                                    application_id=new_application, is_short_answer=0, section_name=i.section_name,
                                                    is_referenced=0, is_exemplar=0)

        # request.session['finish'] = True
        return redirect('coversheet', new_application.pk)
    return render(request, 'success.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['researcher'])
def quiz(request):
    questions = Question.objects.all().filter(is_qualifier_question=1)
    if request.method == 'POST':
        # if one answer is yes, return fail otherwise redirect to ethics welcome.
        for i in range(201, len(questions)+201):
            selection = request.POST.get('selection{}'.format(i))
            if selection == 'Yes':
                return redirect('failure')
        return redirect('success')

    context = {'questions': questions}
    return render(request, 'quiz.html', context)
