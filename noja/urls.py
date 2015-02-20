from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sistdist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^website/', include('website.urls', namespace="website")),
    #url(r'^authentication/', include('login.urls')),
    #url(r'^authentication/logout', include('login.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
