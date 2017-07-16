# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0002_auto_20150715_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='active',
            field=models.BooleanField(verbose_name='aktiv', default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='competition',
            name='command_line_utilities',
            field=models.ManyToManyField(null=True, to='utility.CommandLineUtility', verbose_name='kommandoradsverktyg', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='python_utilities',
            field=models.ManyToManyField(null=True, to='utility.PythonUtility', verbose_name='pythonverktyg', blank=True),
            preserve_default=True,
        ),
    ]
