# -*- coding: utf-8 -*-
import re

from django.core.urlresolvers import reverse, NoReverseMatch
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout

from twitter_user.backends import TwitterBackend
from twitter_user import oauth
from twitter_user import settings

def is_safe_redirect(redirect_to):
    if ' ' in redirect_to:
        return False
    elif '//' in redirect_to and re.match(r'[^\?]*//', redirect_to):
        return False
    return True

def twitter_login(request, redirect_field_name='next'):
    try:
        protocol      = 'https' if request.is_secure() else 'http'
        host          = request.get_host()
        path          = reverse(twitter_callback)
        callback_url  = protocol + '://' + host + path
    except NoReverseMatch:
        callback_url  = None

    consumer      = oauth.Consumer(settings.KEY, settings.SECRET)
    request_token = oauth.RequestToken(consumer, callback_url=callback_url)
    
    request.session['redirect_to'] = "/twitter/feed"
    
    return HttpResponseRedirect(request_token.authorization_url)

def twitter_callback(request):
    backend = TwitterBackend()
    oauth_token    = request.GET['oauth_token']
    oauth_verifier = request.GET['oauth_verifier']
    
    consumer           = oauth.Consumer(settings.KEY, settings.SECRET)
    access_token       = oauth.AccessToken(consumer, oauth_token, oauth_verifier)
    
    user = backend.authenticate(twitter_id   = access_token.user_id,
                                username     = access_token.username,
                                token        = access_token.token,
                                secret       = access_token.secret)

    login(request, user)
    
    redirect_to = request.session['redirect_to']
    if not redirect_to or not is_safe_redirect(redirect_to):
        try:
            redirect_to = reverse(settings.LOGIN_REDIRECT_VIEW, args=[user.id])
        except NoReverseMatch:
            redirect_to = settings.LOGIN_REDIRECT_URL
    
    return HttpResponseRedirect(redirect_to)

def twitter_logout(request, redirect_field_name='next'):
    if request.user.is_authenticated():

        redirect_to = request.REQUEST.get(redirect_field_name, None)
        if not redirect_to or not is_safe_redirect(redirect_to):
            try:
                redirect_to = reverse(settings.LOGOUT_REDIRECT_VIEW, args=[request.user.id])
            except NoReverseMatch:
                redirect_to = settings.LOGOUT_REDIRECT_URL
        
        logout(request)
    else:
        redirect_to = '/'
    
    return HttpResponseRedirect(redirect_to)
