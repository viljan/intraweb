import subprocess
import py_compile
import os
from hashlib import md5
from datetime import datetime

from django.db import models
from django.conf import settings

from .constants import TYPES


def get_filename(instance, filename):
    now = datetime.now()
    base = now.strftime('utility_files/%Y/%m/%d')
    hash = md5(str(now).encode('utf-8'))
    return os.path.join(base, '{}_{}'.format(hash.hexdigest(), filename))

class Utility(models.Model):
    class Meta:
        verbose_name = 'verktyg'
        verbose_name_plural = 'verktyg'

    def __str__(self):
        return self.name

    name = models.CharField('namn', max_length=100)
    description = models.CharField('beskrivning', blank=True, null=True, max_length=100)
    type = models.CharField('typ', choices=TYPES, max_length=100)

class PythonUtility(Utility):
    class Meta:
        verbose_name = 'pythonverktyg'
        verbose_name_plural = verbose_name

    def execute(self):
        filename = self.code.name
        compiled_filename = filename + 'c'
        path = os.path.join(settings.MEDIA_ROOT, filename)
        compiled_path = os.path.join(settings.MEDIA_ROOT, compiled_filename)
        utility_root = os.path.join(settings.MEDIA_ROOT, 'utility_files')

        for root, dirs, files in os.walk(utility_root):
            if not compiled_filename in files:
                try:
                    # Append file at path to 'utility_files/base.py' and then compile the resulting file
                    py_compile.compile(path, cfile=compiled_path, doraise=True)
                except py_compile.PyCompileError:
                    return None
        return compiled_filename

    code = models.FileField('pythonkod', upload_to=get_filename, blank=True, null=True, help_text='En .py-fil med interpreterbar Pythonkod.')

class CommandLineUtility(Utility):
    class Meta:
        verbose_name = 'kommandoradsverktyg'
        verbose_name_plural = verbose_name

    def execute(self):
        cmd = self.command_line.split()
        output = None
        try:
            output = subprocess.check_output(
                cmd,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
        except subprocess.CalledProcessError as e:
            return {
                'success': False,
                'exit_status': e.returncode,
                'output': e.output,
            }

        return {
            'success': True,
            'exit_status': 0,
            'output': output,
        }

    command_line = models.CharField('kommandorad', max_length=100)