# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='utility',
            options={'verbose_name': 'verktyg', 'verbose_name_plural': 'verktyg'},
        ),
        migrations.AddField(
            model_name='utility',
            name='code',
            field=models.TextField(null=True, verbose_name='pythonkod', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='utility',
            name='name',
            field=models.CharField(verbose_name='namn', max_length=100, default='fluff'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='utility',
            name='type',
            field=models.CharField(verbose_name='typ', max_length=100, choices=[('server', 'Server'), ('client', 'Klient')], default='server'),
            preserve_default=False,
        ),
    ]
