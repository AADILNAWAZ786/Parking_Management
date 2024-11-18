# Generated by Django 5.0.3 on 2024-11-18 07:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0005_category_status_alter_add_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add',
            name='add_area_no',
        ),
        migrations.RemoveField(
            model_name='add',
            name='charge',
        ),
        migrations.RemoveField(
            model_name='add',
            name='vehical',
        ),
        migrations.AddField(
            model_name='add',
            name='paring_area_no_id',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='parking.category'),
        ),
        migrations.AddField(
            model_name='add',
            name='parking_charge',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='add',
            name='vehical_Type',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='parking_charge',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]