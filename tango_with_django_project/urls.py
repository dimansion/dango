from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings # New Import
from django.conf.urls.static import static # New Import
from dango import views

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'portofolio.views.index', name='index'),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')), 
    url(r'^dango/', include('dango.urls')),
    url(r'^portofolio/', include('portofolio.urls')), 
    url(r'^dynamicportofolio/', include('dynamicportofolio.urls')),
    url(r'^todo/', include('todo.urls')),
    #url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls')),
)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )

