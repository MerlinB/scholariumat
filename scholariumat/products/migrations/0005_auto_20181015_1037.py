# Generated by Django 2.0.8 on 2018-10-15 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_item_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='price',
            new_name='_price',
        ),
        migrations.AddField(
            model_name='itemtype',
            name='default_price',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]