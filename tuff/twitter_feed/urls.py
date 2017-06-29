from django.conf.urls import url
from twitter_feed.views import *
from django.views.generic import TemplateView

urlpatterns = [
 #   url(r'^$', TemplateView.as_view(template_name='latest_tweets.html')),
    url(r'^$', user_feed),
]
