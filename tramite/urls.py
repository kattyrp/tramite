from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tramite.views.home', name='home'),
    # url(r'^tramite/', include('tramite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
    ),
    url(r'^ver/historial/(?P<documento_id>.*)/$', 'documento.views.list_historial'),
    url(r'^ver/usuario/(?P<area_id>.*)/$', 'documento.views.list_usuario'),
    url(r'^ver/(?P<documento_id>.*)/$', 'documento.views.guardar_documento'),
        # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^search/$', 'documento.views.search')


)