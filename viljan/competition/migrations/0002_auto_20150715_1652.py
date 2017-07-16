# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0005_auto_20150715_1621'),
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='utilities',
        ),
        migrations.AddField(
            model_name='competition',
            name='command_line_utilities',
            field=models.ManyToManyField(to='utility.CommandLineUtility', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competition',
            name='python_utilities',
            field=models.ManyToManyField(to='utility.PythonUtility', null=True, blank=True),
            preserve_default=True,
        ),
    ]
