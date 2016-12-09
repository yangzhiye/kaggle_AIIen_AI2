from django.conf.urls import patterns, include, url
 
from django.contrib import admin
admin.autodiscover()
 
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'hello.views.search'),
    url(r'^search/$', 'hello.views.result'),
    # url(r'^blog/', include('blog.urls')),
 
    url(r'^admin/', include(admin.site.urls)),
)