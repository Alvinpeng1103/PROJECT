from typing import Counter
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.shortcuts import get_object_or_404, render, redirect
from accounts.models import Application, Question, Answers
from django.http import HttpResponse
# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['researcher'])
def questionnaire(request, application_id):
    
    a_id = Application.objects.get(pk=application_id)
    questions = Question.objects.all()
    
    # counter that help to identify if all answers have been answered. 
    counter = 0
    if request.method == 'POST':
    
        ans = Answers.objects.all().filter(application_id = a_id)
        button_name = request.POST.get("Save")
        for i in questions:
            for j in ans:
                if j.question_id == i:
                    # Not a question
                    if i.question_num == 905:
                        break
                    # Let question id change from integer to string
                    que_str = str(i.question_num)
                    template_str = str(j.id)
                    template_text = j.short_answer_text
                    
                        
                    try:
                        # checkbox type question need to get list rather than one
                        if que_str == "702":
                            ans_text = request.POST.getlist("sele1")
                        # checkbox type question need to get list rather than one
                        elif que_str == "901":
                            ans_text = request.POST.getlist("sele2")
                        else:
                            # if it is textarea type question, need extra textarea to store the
                            # template answers and user answers seprately 
                            if i.is_short_answer == 1:
                                template_text = request.POST[template_str]
                                
                            ans_text = request.POST[que_str]
                            
                        #Default for textarea is "", so if user did not answer, counter need to add up by 1
                        if ans_text == "":
                            counter += 1
                    except:
                            #if multiple choice have not been selected, counter add up by 1.
                        counter += 1
                        continue
                    if i.is_short_answer == 1:
                        j.short_answer_text = template_text
                        j.researcher_answer_text = ans_text
                    
                        j.save()
                    else:
                        j.short_answer_text = ans_text
                        j.save()
            
                
        if button_name == "Save":
            a_id.status = "IN PROGRESS"
            a_id.save()
        else:
            a_id.status = "COMPLETE"
            a_id.save()
        
        
        return redirect('managelist')

    que = Question.objects.all()
    answers = Answers.objects.all()
    context = {'que':que, 'answers': answers, 'application_id': application_id, 'a_id': a_id}
    return render(request, 'questionnaire.html', context)