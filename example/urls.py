from django import VERSION
from django.contrib import admin

urlpatterns = []

if VERSION > (2, 0, 0):
    from django.urls import re_path
    urlpatterns.append(re_path(r'^admin/', admin.site.urls))
else:
    from django.conf.urls import url
    urlpatterns.append(url(r'^admin/', admin.site.urls))
