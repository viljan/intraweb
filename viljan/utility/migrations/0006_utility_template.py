# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import viljan.utility.models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0005_auto_20150715_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='utility',
            name='template',
            field=models.FileField(verbose_name='mall', null=True, blank=True, upload_to=viljan.utility.models.get_filename),
            preserve_default=True,
        ),
    ]
