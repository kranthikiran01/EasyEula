from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EasyEula.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', 'auth.views.auth'),
    url(r'^login/', 'auth.views._login'),
    url(r'^logout/', 'auth.views._logout'),
    url(r'^dashboard/', 'eulaX.views.index'),
)
