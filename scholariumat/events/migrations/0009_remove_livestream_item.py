# Generated by Django 2.1.7 on 2019-04-15 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20190415_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livestream',
            name='item',
        ),
    ]