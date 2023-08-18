from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns =[
    path('register_home', views.register_home, name='register_home'),
    path('log_in', views.log_in, name='log_in'),
    path('log_out', views.log_out, name='log_out'),
    path('delete_account', views.delete_account, name='delete_account'),


        # forgot password
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name="password_reset_complete"),
]