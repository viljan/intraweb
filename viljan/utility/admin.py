from django.contrib import admin

from .models import PythonUtility, CommandLineUtility

admin.site.register(PythonUtility)
admin.site.register(CommandLineUtility)