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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout

from viljan.competition import urls as competition_urls
from viljan.library import urls as library_urls
from viljan.utility import urls as utility_urls

from viljan.utility.views import login
from viljan.competition.views import competition_details
from viljan.library.views import media

urlpatterns = [
	url(r'^$', competition_details, name='home'),
	
	url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
	url(r'^logout/$', logout, name='logout'),
	
	url(r'^competition/', include(competition_urls)),
	url(r'^library/', include(library_urls)),
	url(r'^utility/', include(utility_urls)),
	
    url(r'^media/(?P<file_id>\d+)/$', media, name='media'),
    
    url(r'^admin/', include(admin.site.urls)),
]
