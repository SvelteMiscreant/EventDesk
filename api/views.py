from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from event_app.models import *
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from . serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def end_points(request):
    data ={
        "/api/events-list":"get all the events details",
        "/api/group_list":"get all the groups details"

    }
    return Response(data)


@api_view(['GET'])
@permission_classes((IsAdminUser, ))
def events_list(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAdminUser, ))
def group_list(request):
    groups = EventGroup.objects.all()
    serializer = EventGroupSerializer(groups, many=True)
    return Response(serializer.data) 