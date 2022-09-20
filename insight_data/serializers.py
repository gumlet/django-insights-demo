from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=50)

    def create(self, validated_data):
        return Event.objects.create(**validated_data)