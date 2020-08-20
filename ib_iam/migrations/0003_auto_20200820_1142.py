# Generated by Django 2.2.1 on 2020-08-20 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ib_iam', '0002_city_country_elasticuserintermediary_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elasticuserintermediary',
            name='elastic_user_id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='elasticuserintermediary',
            name='user_id',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='elasticuserintermediary',
            unique_together=set(),
        ),
    ]
