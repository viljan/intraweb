from itertools import chain
import re
from datetime import datetime
import os
import subprocess

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as auth_login
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponseForbidden

from viljan.competition.models import Competition

from .constants import BACKUP_PATH, TYPE_SERVER, TYPE_CLIENT
from .models import PythonUtility, CommandLineUtility


def login(request, **kwargs):
    if request.user.is_authenticated():
        return redirect('utility_server')
    else:
        url = request.GET.get('next') or reverse('utility_server')
        return auth_login(request, extra_context={'next': url}, **kwargs)

def utility_client(request, competition_id):
    c = get_object_or_404(Competition, id=competition_id)

    python = c.python_utilities.filter(type=TYPE_CLIENT)
    cmd = c.command_line_utilities.filter(type=TYPE_CLIENT)
    utils = sorted(
        chain(python, cmd),
        key=lambda u: u.name)

    return render(request, 'utility/client.html', {'utilities': utils})

@login_required
def utility_server(request, competition_id):
    c = get_object_or_404(Competition, id=competition_id)

    # Get all related utilities and combine them into a list
    python = c.python_utilities.filter(type=TYPE_SERVER)
    cmd = c.command_line_utilities.filter(type=TYPE_SERVER)
    utils = sorted(
        chain(python, cmd),
        key=lambda u: u.name)

    # Get databases from MySQL
    try:
        output = subprocess.check_output(
            'mysql -e "SHOW DATABASES" -u django -pleffe',
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        )
        expression = re.compile('\n(?!Database|information_schema|performance_schema|mysql)(\w+)')
        databases = expression.findall(output)
    except subprocess.CalledProcessError:
        databases = None

    return render(request, 'utility/server.html', {
        'utilities': utils,
        'databases': databases,
    })

def execute_cmd(request, utility_id):
    if request.user.is_authenticated():
        if request.method == 'POST':
            u = CommandLineUtility.objects.get(id=utility_id)
            return render(request, 'utility/parts/execute_alert.html', u.execute())
        else:
            return HttpResponseNotAllowed(['POST'])
    else:
        return HttpResponseForbidden()

def execute_python(request, utility_id):
    if request.user.is_authenticated():
        u = PythonUtility.objects.get(id=utility_id)
        compiled_filename = u.execute()
        print('u.execute() returns: {}'.format(compiled_filename))
        if compiled_filename:
            return compiled_py(request, compiled_filename)
        else:
            print('execute_python raised Http404')
            raise Http404
    else:
        return HttpResponseForbidden()

def execute_backup(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            db_name = request.POST.get('database', None)
            if not db_name:
                return HttpResponseBadRequest('Databasnamn saknas!')

            cmd = 'mysqldump -u {u} -pleffe --max_allowed_packet=1G --single-transaction=TRUE --result-file="{f}" --databases {db}'
            user = 'django'
            path = os.path.join(BACKUP_PATH, db_name)
            filename = os.path.join(path, datetime.now().strftime('{}_%y%m%d_%H%M%S.sql').format(db_name))

            os.system('mkdir {}'.format(path))
            
            try:
                output = subprocess.check_output(
                    cmd.format(u=user, f=filename, db=db_name),
                    stderr=subprocess.STDOUT,
                    universal_newlines=True,
                )
            except subprocess.CalledProcessError as e:
                return render(request, 'utility/parts/execute_alert.html', {
                    'success': False,
                    'exit_status': e.returncode,
                    'output': e.output,
                })

            return render(request, 'utility/parts/execute_alert.html', {
                'success': True,
                'exit_status': 0,
                'output': output,
            })
        else:
            return HttpResponseNotAllowed(['POST'])
    else:
        return HttpResponseForbidden()

def execute_restore(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            db_name = request.POST.get('database', None)
            backup_name = request.POST.get('backup', None)
            if not db_name or not backup_name:
                return HttpResponseBadRequest('Ogiltiga parametrar!')

            cmd = 'mysql -u {u} -pleffe {db} < {b}'
            user = 'django'
            path = os.path.join(BACKUP_PATH, db_name, backup_name)

            try:
                output = subprocess.check_output(
                    cmd.format(u=user, b=path, db=db_name),
                    stderr=subprocess.STDOUT,
                    universal_newlines=True,
                    shell=True
                )
            except subprocess.CalledProcessError as e:
                return render(request, 'utility/parts/execute_alert.html', {
                    'success': False,
                    'exit_status': e.returncode,
                    'output': e.output,
                })

            return render(request, 'utility/parts/execute_alert.html', {
                'success': True,
                'exit_status': 0,
                'output': output,
            })
        else:
            return HttpResponseNotAllowed(['POST'])
    else:
        return HttpResponseForbidden()

def backup_list(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            db_name = request.POST.get('database', None)
            if not db_name:
                return HttpResponseBadRequest('Databasnamn saknas!')

            try:
                path = os.path.join(BACKUP_PATH, db_name)
                files = [file for file in os.listdir(path)]
                format = '{}_%y%m%d_%H%M%S.sql'.format(db_name)
                backups = ((file, datetime.strptime(file, format)) for file in files)
            except FileNotFoundError:
                backups = None

            return render(request, 'utility/parts/backup_options.html', {
                'backups': backups
            })
        else:
            return HttpResponseNotAllowed(['POST'])
    else:
        return HttpResponseForbidden()

def compiled_py(request, path):
    print(os.path.join(settings.MEDIA_ROOT, path))
    try:
        fd = open(os.path.join(settings.MEDIA_ROOT, path), 'rb')
    except FileNotFoundError:
        print('compiled_py raised Http404')
        raise Http404

    response = HttpResponse(content=fd.read())
    extension = path.split('.')[-1]
    path = path.split('_')[-1]
    response['Content-Type'] = 'application/' + extension
    response['Content-Disposition'] = 'attachment; filename=' + path

    return response