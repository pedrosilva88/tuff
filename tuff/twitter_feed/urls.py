from django.conf.urls import url
from twitter_feed.views import *
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', user_feed),
]
