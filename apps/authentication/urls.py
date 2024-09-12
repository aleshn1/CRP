# -*- encoding: utf-8 -*-
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from .forms import LoginForm
from .views import show_user_profile, update_profile_data, password_reset_request, forgot_password_request

urlpatterns = [
    path('accounts/login/', LoginView.as_view(authentication_form=LoginForm), name='login'),

    path('login/', LoginView.as_view(authentication_form=LoginForm), name='login'),

    path("logout/", LogoutView.as_view(), name="logout"),

    path('user_profile/', show_user_profile, name="user_profile"),

    path('update_profile/<str:pk>', update_profile_data, name="update_profile"),

    path("password_reset/", password_reset_request, name="password_reset"),

    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('change_password/', auth_views.PasswordChangeView.as_view(
        template_name='registration/change_password.html', success_url='/password_change_done/'),
         name='change_password'),

    path('forgot_password/', forgot_password_request, name='forgot_password'),

    path("password_reset", password_reset_request, name="password_reset"),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password/password_reset_done.html'),
         name='password_reset_done'),

    path('forgot_password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/forgot_password/password_reset_done.html'),
         name='forgot_password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="registration/password/password_reset_confirm.html"),
         name='password_reset_confirm'),  # Redefinição de senha do perfil do usuario

    path('reset_forgot_password/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="registration/forgot_password/forgot_password_reset_confirm.html"),
         name='forgot_password_reset_confirm'),  # Redefinição de senha do 'Esqueceu a senha?'

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password/password_reset_complete.html'), name='password_reset_complete'),
]
