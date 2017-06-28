from django.conf.urls import url
from twitter_user.views import *

urlpatterns = [
    url(r'^login/?$',           twitter_login),
    url(r'^login/callback/?$',  twitter_callback),
    url(r'^logout/?$',          twitter_logout),
]

#    url(r'^login/?$', twitter_login),
