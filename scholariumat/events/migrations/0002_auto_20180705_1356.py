# Generated by Django 2.0.5 on 2018-07-05 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livestream',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.Item'),
        ),
        migrations.AddField(
            model_name='event',
            name='product',
            field=models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.EventType'),
        ),
    ]
