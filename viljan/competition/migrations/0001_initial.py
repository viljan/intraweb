# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import viljan.competition.models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0001_initial'),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='namn', max_length=100)),
                ('eventor_id', models.PositiveIntegerField(verbose_name='Eventor-ID')),
                ('library', models.ForeignKey(default=viljan.competition.models.get_new_library, to='library.Library')),
                ('utilities', models.ManyToManyField(null=True, blank=True, to='utility.Utility')),
            ],
            options={
                'verbose_name': 'tävling',
                'verbose_name_plural': 'tävlingar',
            },
            bases=(models.Model,),
        ),
    ]
