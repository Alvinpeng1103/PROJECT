from django.shortcuts import render
from accounts.models import Application
from django.views.generic import DetailView, UpdateView
from .utils import render_to_pdf
from django.shortcuts import render, redirect
from .forms import PISform, PCFform
from django.contrib.auth.decorators import login_required
#lock behind authentication barrier

#view participant information statement
@login_required(login_url='login')
def PISform2(request, application_id):
    context ={
        'data': Application.objects.get(pk=application_id),
        'application_id': application_id
    }
    pdf = render_to_pdf('information_sheet.html', context) #view form as PDF
    return pdf

#view participant consent form
@login_required(login_url='login')
def PCFform2(request, application_id):
    context ={
        'data': Application.objects.get(pk=application_id),
        'application_id': application_id
    }
    pdf = render_to_pdf('consent_form.html', context) #view form as PDF
    return pdf

#creation of participant information statement
@login_required(login_url='login')
def createPIS(request, application_id):
    form = PISform(instance=Application.objects.get(pk=application_id)) #retrieving form from forms.py
    if request.method == 'POST': #save form if it is valid and "submit" is pressed
        form = PISform(request.POST, instance=Application.objects.get(pk=application_id))
        if form.is_valid():
            form.save(commit=True)
    context = {
        'form':form,
        'application_id': application_id
    }
    return render(request, 'new_PIS.html', context)

#creation of participant consent form
@login_required(login_url='login')
def createPCF(request, application_id):
    form = PCFform(instance=Application.objects.get(pk=application_id)) #retrieving form from forms.py
    if request.method == 'POST': #save form if it is valid and "submit" is pressed
        form = PCFform(request.POST, instance=Application.objects.get(pk=application_id))
        if form.is_valid():
            form.save(commit=True)
    context = {
        'form':form,
        'application_id': application_id
    }
    return render(request, 'new_PCF.html', context) 




