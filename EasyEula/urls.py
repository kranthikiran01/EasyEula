from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EasyEula.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', 'authentication.views.auth'),
    url(r'^login/', 'authentication.views._login'),
    url(r'^logout/', 'authentication.views._logout'),
    url(r'^register/','authentication.views.register'),
    url(r'^dashboard/', 'eulaX.views.index'),
    url(r'^newdocument/', 'eulaX.views.document'),
    url(r'^listdocuments/','eulaX.views.listDocuments'),
    url(r'^view/(?P<slug>[^\.]+).html','eulaX.views.viewDocument',name='view_document'),
    url(r'^ckeditor/', include('ckeditor.urls')),
)


from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)

