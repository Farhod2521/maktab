from rest_framework import serializers
from .models import GameLevel

class GameLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameLevel
        fields = '__all__'