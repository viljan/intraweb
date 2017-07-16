from django.contrib import admin

from .models import Library, Application, Driver, Document

admin.site.register(Library)
admin.site.register(Application)
admin.site.register(Driver)
admin.site.register(Document)
