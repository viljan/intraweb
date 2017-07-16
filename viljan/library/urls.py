from django.conf.urls import url

from .views import library_details, application_list, driver_list, document_list

urlpatterns = [
	url(r'^(?P<library_id>\d+)/$', library_details, name='library_details'),
	url(r'^(?P<library_id>\d+)/applications/$', application_list, name='application_list'),
	url(r'^(?P<library_id>\d+)/drivers/$', driver_list, name='driver_list'),
	url(r'^(?P<library_id>\d+)/documents/$', document_list, name='document_list'),
]
