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

from viljan.utility.views import utility_server, utility_client

from .views import competition_details, library_redirect, eventor

urlpatterns = [
	url(r'^$', competition_details, name='competition_details'),
	url(r'^(?P<competition_id>\d+)/library/$', library_redirect, {'url_name': 'library_details'}, name='competition_library'),
	url(r'^(?P<competition_id>\d+)/applications/$', library_redirect, {'url_name': 'application_list'}, name='competition_applications'),
	url(r'^(?P<competition_id>\d+)/drivers/$', library_redirect, {'url_name': 'driver_list'}, name='competition_drivers'),
	url(r'^(?P<competition_id>\d+)/documents/$', library_redirect, {'url_name': 'document_list'}, name='competition_documents'),
	url(r'^(?P<competition_id>\d+)/server/$', utility_server, name='utility_server'),
	url(r'^(?P<competition_id>\d+)/client/$', utility_client, name='utility_client'),
	url(r'^eventor/$', eventor, name='eventor'),
]
