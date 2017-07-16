# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import viljan.utility.models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0006_utility_template'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pythonutility',
            name='executable_code',
        ),
        migrations.RemoveField(
            model_name='pythonutility',
            name='validation_code',
        ),
        migrations.RemoveField(
            model_name='utility',
            name='template',
        ),
        migrations.AddField(
            model_name='pythonutility',
            name='code',
            field=models.FileField(blank=True, verbose_name='pythonkod', null=True, upload_to=viljan.utility.models.get_filename, help_text='En .py-fil med interpreterbar Pythonkod.'),
            preserve_default=True,
        ),
    ]
