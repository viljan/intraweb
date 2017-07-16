from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

from viljan.competition.models import Competition


def competition(request):
    try:
        c = Competition.objects.get(active=True)
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        c = None

    return {'competition': c}