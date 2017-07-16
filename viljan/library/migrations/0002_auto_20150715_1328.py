# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': 'programvara', 'verbose_name_plural': 'programvaror'},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'dokument', 'verbose_name_plural': 'dokument'},
        ),
        migrations.AlterModelOptions(
            name='driver',
            options={'verbose_name': 'drivrutin', 'verbose_name_plural': 'drivrutiner'},
        ),
        migrations.AlterModelOptions(
            name='software',
            options={'verbose_name': 'dokument', 'verbose_name_plural': 'dokument'},
        ),
    ]
