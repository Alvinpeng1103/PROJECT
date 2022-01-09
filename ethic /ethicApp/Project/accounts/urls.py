from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# URLconf
urlpatterns = [
    path('', views.redirect_view),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('edit_profile/', views.editUserPage, name='editprofile'),
    ##Password reset##
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"), name="password_reset_complete"),
]
