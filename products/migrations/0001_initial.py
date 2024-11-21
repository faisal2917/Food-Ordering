# Generated by Django 5.1.3 on 2024-11-21 08:25

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_slug', models.SlugField(unique=True)),
                ('product_description', models.TextField()),
                ('product_price', models.IntegerField(default=0)),
                ('product_actual_price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_images', models.ImageField(upload_to='products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMetaInformation',
            fields=[
                ('updated_at', models.DateField(auto_created=True)),
                ('created_at', models.DateField(auto_created=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_measuring', models.CharField(blank=True, choices=[('KG', 'KG'), ('ML', 'ML'), ('L', 'L'), (None, None)], max_length=100, null=True)),
                ('product_quantity', models.CharField(blank=True, max_length=5, null=True)),
                ('is_restrict', models.BooleanField(default=False)),
                ('restrict_quantity', models.IntegerField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='meta_information', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
