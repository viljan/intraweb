import os

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Library, File


def library_details(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    return render(request, 'library/details.html', {'library': library})

def application_list(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    return render(request, 'library/application_list.html', {'library': library.applications.all})

def driver_list(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    return render(request, 'library/driver_list.html', {'library': library.drivers.all})

def document_list(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    return render(request, 'library/document_list.html', {'library': library.documents.all})

def media(request, file_id):
    file = get_object_or_404(File, id=file_id)
    try:
        fd = open(os.path.join(settings.MEDIA_ROOT, file.data.name), 'rb')
    except FileNotFoundError:
        raise Http404

    response = HttpResponse(content=fd.read())
    extension = file.data.name.split('.')[-1]
    filename = file.data.name.split('_')[-1]
    response['Content-Type'] = 'application/' + extension
    response['Content-Disposition'] = 'attachment; filename=' + filename

    return response
