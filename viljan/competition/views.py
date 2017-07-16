from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Competition


def competition_details(request):
    return render(request, 'competition/details.html', {})

def library_redirect(request, competition_id, url_name):
    c = get_object_or_404(Competition, id=competition_id)
    return redirect(reverse(url_name, args=[c.library_id]), permanent=True)

def eventor(request, competition_id):
    c = get_object_or_404(Competition, id=competition_id)
    return redirect('http://eventor.orientering.se/Events/Show/' + c.eventor_id, permanent=True)