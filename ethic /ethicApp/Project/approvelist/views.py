from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.decorators import allowed_users
from accounts.models import Answers, Application
from accounts.models import Question
# Create your views here.



def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['staff'])
def approve(request, item_id):

    item = Application.objects.get(pk=item_id)
    item.status = 'APPROVED'
    item.save()

    return redirect('approvelist')


@login_required(login_url='login')
@allowed_users(allowed_roles=['staff'])
def disapprove(request, item_id):

    
    item = Application.objects.get(pk=item_id)
    item.status = 'DISAPPROVED'
    item.save()

    return redirect('approvelist')


@login_required(login_url='login')
@allowed_users(allowed_roles=['staff'])
def viewPage(request, item_id):
    que = Question.objects.all()
    
    a_id = Application.objects.get(pk=item_id)
    answers = Answers.objects.all().filter(application_id=a_id)

    context = {'que': que, 'answers': answers, 'a_id':a_id}
    return render(request, 'view.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['staff'])
def approvelistPage(request):

    applications = Application.objects.all()

    context = {'applications': applications}
    return render(request, 'approvelist.html', context)
