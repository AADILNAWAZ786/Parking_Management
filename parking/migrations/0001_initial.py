# Generated by Django 5.0.3 on 2024-03-07 05:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_vehical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.CharField(max_length=11)),
                ('vehical_no', models.CharField(max_length=200)),
                ('paring_area_no', models.CharField(max_length=100)),
                ('vehical_type', models.CharField(max_length=100)),
                ('parking_charge', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.CharField(max_length=11)),
                ('paring_area_no', models.CharField(max_length=100)),
                ('vehical_type', models.CharField(max_length=100)),
                ('vehical_limit', models.CharField(max_length=200)),
                ('parking_charge', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
