from rest_framework import serializers
from clubs.models import club_detail
class ClublistSerializer(serializers.ModelSerializer):
    class Meta:
        model = club_detail
        fields ='__all__'