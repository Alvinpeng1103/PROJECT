from django.urls import path
from . import views
from accounts.views import editUserPage

urlpatterns = [
    path('', views.managelistPage, name='managelist'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', editUserPage, name='editprofile'),
    path('<int:item_id>/', views.deleteRow, name='delete'),
    path('view/<item_id>', views.viewNormal, name='viewNormal'),
]
