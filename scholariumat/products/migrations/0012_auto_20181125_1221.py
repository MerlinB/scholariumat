# Generated by Django 2.0.9 on 2018-11-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20181123_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='amount',
            new_name='_amount',
        ),
        migrations.AddField(
            model_name='itemtype',
            name='default_amount',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]