from django.urls import path
from . import views

urlpatterns = [
  path('<application_id>', views.questionnaire, name="questionnaire"),
]