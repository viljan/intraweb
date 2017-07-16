# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0004_auto_20150715_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommandLineUtility',
            fields=[
                ('utility_ptr', models.OneToOneField(parent_link=True, primary_key=True, to='utility.Utility', auto_created=True, serialize=False)),
                ('command_line', models.CharField(max_length=100, verbose_name='kommandorad')),
            ],
            options={
                'verbose_name_plural': 'kommandoradsverktyg',
                'verbose_name': 'kommandoradsverktyg',
            },
            bases=('utility.utility',),
        ),
        migrations.CreateModel(
            name='PythonUtility',
            fields=[
                ('utility_ptr', models.OneToOneField(parent_link=True, primary_key=True, to='utility.Utility', auto_created=True, serialize=False)),
                ('executable_code', models.TextField(verbose_name='pythonkod')),
                ('validation_code', models.TextField(verbose_name='valideringskod')),
            ],
            options={
                'verbose_name_plural': 'pythonverktyg',
                'verbose_name': 'pythonverktyg',
            },
            bases=('utility.utility',),
        ),
        migrations.RemoveField(
            model_name='utility',
            name='execute_code',
        ),
        migrations.RemoveField(
            model_name='utility',
            name='validate_code',
        ),
    ]
