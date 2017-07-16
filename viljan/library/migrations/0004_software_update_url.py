# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20150715_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='update_url',
            field=models.URLField(null=True, verbose_name='länk till uppdatering', blank=True),
            preserve_default=True,
        ),
    ]
