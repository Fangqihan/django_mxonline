from django.conf.urls import url, include
from django.contrib import admin

from app1.views import test


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', test),
    url(r'^api/', include('app1.urls')),

]


from django.views.static import serve
from django import conf

urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': conf.settings.MEDIA_ROOT,
    }),
]




