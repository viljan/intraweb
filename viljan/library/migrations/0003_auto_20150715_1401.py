# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20150715_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='describes',
        ),
        migrations.AddField(
            model_name='file',
            name='description',
            field=models.CharField(max_length=100, blank=True, null=True, verbose_name='beskrivning'),
            preserve_default=True,
        ),
    ]
