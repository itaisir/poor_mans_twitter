from django.conf.urls import url
from .views import *

urlpatterns = [
    url('tweet/$',TweetView.as_view(),name="add_get_all_tweet"),
]