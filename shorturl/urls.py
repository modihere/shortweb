from django.conf.urls import include, url
from . import views
 
urlpatterns = [
    url(r'^$', views.index,name='home'),
    # for our home/index pag1e
 
    url(r'^(?P<short_id>\w{3,6})$', views.redirect_original, name='redirectoriginal'),
    # when short URL is requested it redirects to original URL
 
    url(r'^makeshort/$', views.shorten_url, name='shortenurl'),
    # this will create a URL's short id and return the short URL
    ]
