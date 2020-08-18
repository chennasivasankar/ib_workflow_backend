# Generated by Django 2.2.1 on 2020-08-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ib_iam', '0002_city_country_elasticuserintermediary_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
