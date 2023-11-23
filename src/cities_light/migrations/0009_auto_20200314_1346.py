# Generated by Django 2.2.1 on 2020-03-14 13:46

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0008_city_timezone'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='location_map',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='country',
            name='location_map',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='region',
            name='code2',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='location_map',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326),
        ),
    ]