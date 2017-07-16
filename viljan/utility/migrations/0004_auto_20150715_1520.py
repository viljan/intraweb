# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0003_utility_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utility',
            old_name='code',
            new_name='execute_code',
        ),
        migrations.AddField(
            model_name='utility',
            name='validate_code',
            field=models.TextField(blank=True, verbose_name='valideringskod', null=True),
            preserve_default=True,
        ),
    ]
