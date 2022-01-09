from django.urls import path
from . import views

urlpatterns = [
    path('', views.approvelistPage, name='approvelist'),
    path('logout/', views.logout_view, name='logout'),
    path('approve/<item_id>', views.approve, name='approve'),
    path('disapprove/<item_id>', views.disapprove, name='disapprove'),
    path('view/<item_id>', views.viewPage, name='viewPage')
]
