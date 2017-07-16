# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0002_auto_20150715_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='utility',
            name='description',
            field=models.CharField(verbose_name='beskrivning', null=True, max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
