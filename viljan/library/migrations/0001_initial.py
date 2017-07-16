# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import viljan.library.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='namn', max_length=100)),
                ('data', models.FileField(verbose_name='data', upload_to=viljan.library.models.get_filename)),
                ('uploaded_at', models.DateTimeField(auto_now=True, verbose_name='uppladdad')),
                ('version', models.CharField(null=True, blank=True, max_length=20, verbose_name='version')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('file_ptr', models.OneToOneField(to='library.File', serialize=False, parent_link=True, primary_key=True, auto_created=True)),
                ('describes', models.CharField(verbose_name='beskriver', max_length=100)),
            ],
            options={
            },
            bases=('library.file',),
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(null=True, blank=True, max_length=100, verbose_name='namn')),
            ],
            options={
                'verbose_name': 'filbibliotek',
                'verbose_name_plural': 'filbibliotek',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('file_ptr', models.OneToOneField(to='library.File', serialize=False, parent_link=True, primary_key=True, auto_created=True)),
            ],
            options={
            },
            bases=('library.file',),
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('software_ptr', models.OneToOneField(to='library.Software', serialize=False, parent_link=True, primary_key=True, auto_created=True)),
                ('used_for', models.CharField(null=True, blank=True, max_length=100, verbose_name='används till')),
            ],
            options={
            },
            bases=('library.software',),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('software_ptr', models.OneToOneField(to='library.Software', serialize=False, parent_link=True, primary_key=True, auto_created=True)),
                ('developer', models.CharField(null=True, blank=True, max_length=100, verbose_name='utvecklare')),
            ],
            options={
            },
            bases=('library.software',),
        ),
        migrations.AddField(
            model_name='software',
            name='documents',
            field=models.ManyToManyField(null=True, blank=True, verbose_name='dokument', to='library.Document'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='library',
            name='applications',
            field=models.ManyToManyField(null=True, related_name='library', blank=True, verbose_name='programvaror', to='library.Application'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='library',
            name='documents',
            field=models.ManyToManyField(null=True, related_name='library', blank=True, verbose_name='dokumentation', to='library.Document'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='library',
            name='drivers',
            field=models.ManyToManyField(null=True, related_name='library', blank=True, verbose_name='drivrutiner', to='library.Driver'),
            preserve_default=True,
        ),
    ]
