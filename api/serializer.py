from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import gameLog


class gameLogSerializer(ModelSerializer):
    class Meta:
        model = gameLog
        fields = "__all__"
