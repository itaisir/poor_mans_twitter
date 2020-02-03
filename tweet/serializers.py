from rest_framework import serializers
from .models import *


class TweetSerializer(serializers.ModelSerializer):
    datetime = serializers.DateTimeField(
        read_only=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Tweet
        fields = ('name', 'message', 'datetime',)
