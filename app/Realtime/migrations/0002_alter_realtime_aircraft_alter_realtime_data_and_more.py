# Generated by Django 4.0.6 on 2022-09-18 18:37

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Realtime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtime',
            name='aircraft',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Realtime.aircraft'),
        ),
        migrations.AlterField(
            model_name='realtime',
            name='data',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=5, max_digits=10), size=None), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='realtime',
            name='flight_mode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Realtime.flightmode'),
        ),
        migrations.AlterField(
            model_name='realtime',
            name='height',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=5, max_digits=10), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='realtime',
            name='hopper_outlet_size',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=5, max_digits=10), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='realtime',
            name='spinner_disk_speed',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=5, max_digits=10), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='realtime',
            name='spraying_rate',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=5, max_digits=10), null=True, size=None),
        ),
    ]
