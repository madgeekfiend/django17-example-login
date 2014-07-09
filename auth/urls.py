from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #login & log out
    url(r'^login/$', 'django.contrib.auth.views.login'),

    url(r'^$', include('authexample.urls')),
    url(r'^admin/', include(admin.site.urls)),



)
