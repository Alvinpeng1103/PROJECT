from django.urls import path
from . import views
from .views import PISform2, PCFform2, createPIS, createPCF

urlpatterns = [
    #path('PIS/<int:pk>', PISform2.as_view(), name='information_sheet'),
    path('PIS/<application_id>', views.PISform2, name='information_sheet'),
    path('PCF/<application_id>', views.PCFform2, name='consent_form'),
    #path('PCF/<int:pk>', PCFform2.as_view(), name='consent_form'),
    #path('new_PIS/<int:pk>', createPIS.as_view(), name='new_PIS'),
    #path('new_PCF/<int:pk>', createPCF.as_view(), name='new_PCF'),
    path('newPIS<application_id>', views.createPIS, name='new_PIS'),
    path('newPCF<application_id>', views.createPCF, name='new_PCF'),
]