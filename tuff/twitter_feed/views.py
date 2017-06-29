# -*- coding: utf-8 -*-
import re

from django.core.urlresolvers import reverse, NoReverseMatch
from django.http import HttpResponseRedirect, HttpResponse

from django.template import loader
from twitter_feed.models import Tweet

def user_feed(request, redirect_field_name='next'):
    if request.user.is_authenticated():
    	objects = Tweet.objects.all()
        template = loader.get_template('twitter_feed/latest_tweets.html')
    	context = {
        	'tweets': objects,
    	}
    else:
        return HttpResponseRedirect(redirect_to)
    
    return HttpResponse(template.render(context, request))