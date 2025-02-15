# Generated by Django 3.0.5 on 2020-05-08 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0010_add_subregion'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='city',
            unique_together={('region', 'subregion', 'slug'), ('region', 'subregion', 'name')},
        ),
        migrations.AlterField(
            model_name='subregion',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='cities_light.Region'),
        ),
    ]
