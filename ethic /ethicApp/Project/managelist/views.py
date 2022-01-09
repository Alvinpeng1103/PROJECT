from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.shortcuts import render, redirect
from accounts.models import Application
from accounts.models import Answers, Application
from accounts.models import Question

# PDF generation imports
from django.http import FileResponse
import io
from .utils import render_to_pdf
# Create your views here.



def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['researcher'])
def managelistPage(request):

    applications = Application.objects.filter(user=request.user)
    
    context = {'applications': applications}  

    return render(request, 'managelist.html', context)



    

@login_required(login_url='login')
@allowed_users(allowed_roles=['researcher'])

def deleteRow(request, item_id):

    item = Application.objects.get(pk=item_id)

    item.delete()

    return redirect('managelist')

@login_required(login_url='login')
@allowed_users(allowed_roles=['researcher'])
def viewNormal(request, item_id):
    que = Question.objects.all()
    
    a_id = Application.objects.get(pk=item_id)
    answers = Answers.objects.all().filter(application_id=a_id)

    context = {'que': que, 'answers': answers, 'a_id':a_id}
    #return render(request, 'viewNormal.html', context)
    pdf = render_to_pdf('viewNormal.html', context)
    return pdf
    







