from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome, name="qualifierwelcome"),
    path('quiz/', views.quiz, name="quiz"),
    path('failure/', views.failure, name="failure"),
    path('success/', views.success, name="success")
]
