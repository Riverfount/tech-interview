from django.contrib import admin
from django.urls import include, path

from .core import urls

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/v1/', include(urls), name='api'),
]
