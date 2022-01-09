from django.urls import path
from . import views
from accounts.views import editUserPage
from questionnaire.views import questionnaire
from viewforms.views import PISform2, PCFform2, createPIS, createPCF

urlpatterns = [
    path('<newapplication_id>', views.coversheetPage, name='coversheet'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', editUserPage, name='editprofile'),
    path('<application_id>', questionnaire, name="questionnaire"),
    
    path('PIS/<int:pk>', PISform2, name='information_sheet'),
    path('PCF/<int:pk>', PCFform2, name='consent_form'),
    path('new_PIS/<int:pk>', createPIS, name='new_PIS'),
    path('new_PCF/<int:pk>', createPCF, name='new_PCF'),
]
