from django.shortcuts import render
from django.http import Http404
from django.urls import reverse

from rest_framework import permissions, status
from rest_framework import generics
from .serializers import *
from .models import *


class TweetView(generics.ListCreateAPIView):
    queryset = Tweet.objects.order_by('-datetime').all()
    serializer_class = TweetSerializer
    permission_classes = (permissions.AllowAny,)


