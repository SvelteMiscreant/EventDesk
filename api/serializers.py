from rest_framework import serializers
from event_app.models import *




class EventSerializer(serializers.ModelSerializer):
    host_name = serializers.CharField(source='host.user.username')
    # group_name = serializers.CharField(source='group.name')
    class Meta:
        model = Event
        fields = ['title', 'description','host_name', 'poster', 'rules', 'type_of', 'group', 'no_of_participants', 'start_time', 'end_time' ]
        depth = 1


class EventGroupSerializer(serializers.ModelSerializer):
    creator_name = serializers.CharField(source='creator.user.username')
    class Meta:
        model = EventGroup
        fields = ['name','description','poster', 'creator_name', 'restricted', 'created_time']
        depth = 1 