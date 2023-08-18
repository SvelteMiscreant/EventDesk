from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('', views.home, name="home"),
    path('add_event', views.add_event, name="add_event"),
    path('edit_event/<int:pk>', views.edit_event, name="edit_event"),
    path('add_form_parent/<int:pk>', views.add_form_parent, name="add_form_parent"),
    path('add_form_fields/<int:pk>', views.add_form_fields, name="add_form_fields"),
    path('delete_form_field/<int:pk>', views.delete_form_field, name='delete_form_field'),
    path('event_view_host/<int:pk>', views.event_view_host, name='event_view_host'),
    path('responses/<int:pk>', views.responses, name='responses'),
    path('event_home/<int:pk>', views.event_home, name='event_home'),
    path('form_view/<str:unique_id>', views.form_view, name='form_view'),
    path('form_submit/<str:unique_id>', views.form_submit,name="form_submit"),
    path('accept_responses_toggle/<int:pk>', views.accept_responses_toggle, name='accept_responses_toggle'),
   
    path('winner_declaration/<str:unique_id>', views.winner_declaration, name='winner_declaration'),
    path('send_mail_to_winners/<str:unique_id>', views.send_mail_to_winners, name='send_mail_to_winners'),
    path('send_mail_to_participants/<str:unique_id>', views.send_mail_to_participants, name='send_mail_to_participants'),
    # path('register_home', views.register_home, name='register_home'),
    # path('log_in', views.log_in, name='log_in'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('events_list_host', views.events_list_host, name='events_list_host'),
    path('groups_list_host', views.groups_list_host, name='groups_list_host'),
    path('contact_host/<int:pk>', views.contact_host, name='contact_host'),
    path('delete_event/<int:pk>', views.delete_event, name='delete_event'),
    path('delete_group/<int:pk>', views.delete_group, name='delete_group'),
    path('add_group_event/<int:id>', views.add_group_event, name='add_group_event'),
    path('add_group', views.add_group,name='add_group'),
    path('group_view/<int:pk>', views.group_view, name="group_view"),
    path('all_events', views.all_events, name='all_events'),
    path('all_groups', views.all_groups, name='all_groups'),
    path('profile_edit', views.profile_edit,name='profile_edit'),
    path('tagged_events/<int:pk>', views.tagged_events, name="tagged_events"),
    path('sub_to_nl', views.sub_to_nl, name='sub_to_nl'),
    # path('log_out', views.log_out, name='log_out'),
    path('terms_and_policy', views.terms_and_policy, name='terms_and_policy'),
    path('about', views.about, name='about'),
    path('chat_room/<int:pk>', views.chat_room, name="chat_room"),
    path('send_chat/', views.send_chat, name='send_chat'),
    path('load_chat/<int:room_id>', views.load_chat, name='load_chat'),
    path('submit_feedback', views.submit_feedback, name='submit_feedback'),
    # path('delete_account', views.delete_account, name='delete_account'),




    # forgot password
    # path('reset_password', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name="reset_password"),
    # path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name='password_reset_confirm'),
    # path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name="password_reset_complete"),



]