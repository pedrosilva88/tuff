from django.conf.urls import include, url
from django.views.generic import TemplateView
import twitter_user.urls
import twitter_feed.urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^twitter/', include('twitter_user.urls')),
    url(r'^twitter/feed', include('twitter_feed.urls')),

]

#if settings.DEBUG:
    #import debug_toolbar
    #urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
