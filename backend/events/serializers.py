from rest_framework import serializers
from events.models import event
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields ='__all__'


class UpdateEventSerializer(serializers.ModelSerializer):
    class Meat:
        model = event
        fields = (
            'event_description',
            'event_date',
            'event_end',
            'event_poster',
        )