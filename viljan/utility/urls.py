"""viljan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

from .views import execute_cmd, execute_python, execute_backup, execute_restore, backup_list


urlpatterns = [
	url(r'^cmd(?P<utility_id>\d+)/execute/$', execute_cmd, name='execute_command_line'),
	url(r'^python(?P<utility_id>\d+)/execute/$', execute_python, name='execute_python'),
    url(r'^backup/execute/$', execute_backup, name='backup'),
	url(r'^restore/execute/$', execute_restore, name='restore'),
	url(r'^restore/backups/$', backup_list),
]
