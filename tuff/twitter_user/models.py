# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class TwitterUser(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200, default="no name")
    oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)
