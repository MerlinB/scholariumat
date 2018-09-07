# Generated by Django 2.0.8 on 2018-09-07 11:45

import datetime
from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
                ('publish_date', models.DateField(blank=True, null=True)),
                ('priority', models.PositiveSmallIntegerField(default=0)),
                ('date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Veranstaltung',
                'verbose_name_plural': 'Veranstaltungen',
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Veranstaltungsart',
                'verbose_name_plural': 'Veranstaltungsarten',
            },
        ),
        migrations.CreateModel(
            name='Livestream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('link', models.CharField(max_length=100)),
                ('chat', models.BooleanField(default=False)),
                ('time_start', models.TimeField(default=datetime.time(19, 0))),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
