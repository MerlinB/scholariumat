# Generated by Django 2.0.7 on 2018-08-01 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180721_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemtype',
            name='slug',
            field=models.SlugField(),
        ),
    ]