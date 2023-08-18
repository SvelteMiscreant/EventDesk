from django.urls import path

from . import views
from rest_framework.authtoken.views  import obtain_auth_token
urlpatterns = [
    path('end-points/', views.end_points, name='endpoints'),
    path("events-list/", views.events_list, name="events-list" ),
    path("group-list/", views.group_list, name="group-list"),
    path('auth-token/', obtain_auth_token),
] 