# Generated by Django 2.0.7 on 2018-08-04 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180801_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='applied',
            new_name='executed',
        ),
    ]