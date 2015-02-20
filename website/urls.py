#urls de web pedidos

from django.conf.urls import patterns, url

from website import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    url(r'^/$', 'website.views.index'),
    #url(r'^/login/$', 'web_pedidos.views.login'),
)