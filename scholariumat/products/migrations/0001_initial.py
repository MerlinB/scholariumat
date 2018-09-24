# Generated by Django 2.0.8 on 2018-09-24 11:51

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttachmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Anhangstyp',
                'verbose_name_plural': 'Anhangstypen',
            },
        ),
        migrations.CreateModel(
            name='FileAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Anhang',
                'verbose_name_plural': 'Anhänge',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('price', models.SmallIntegerField(blank=True, null=True, verbose_name='Preis')),
                ('amount', models.IntegerField(blank=True, null=True, verbose_name='Anzahl')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', models.SlugField()),
                ('shipping', models.BooleanField(default=False)),
                ('requestable', models.BooleanField(default=False)),
                ('purchasable_at', models.SmallIntegerField(default=0)),
                ('accessible_at', models.SmallIntegerField(blank=True, null=True)),
                ('unavailability_notice', models.CharField(default='Nicht verfügbar', max_length=20)),
            ],
            options={
                'verbose_name': 'Item Typ',
                'verbose_name_plural': 'Item Typen',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Produkt',
                'verbose_name_plural': 'Produkte',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('comment', models.TextField(blank=True)),
                ('amount', models.SmallIntegerField(default=1)),
                ('shipped', models.DateField(blank=True, null=True)),
                ('executed', models.BooleanField(default=False)),
                ('free', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Item')),
            ],
            options={
                'verbose_name': 'Kauf',
                'verbose_name_plural': 'Käufe',
            },
        ),
    ]
