# Generated by Django 2.2.1 on 2020-08-08 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ib_discussions', '0003_auto_20200808_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='user_id',
            field=models.CharField(max_length=250),
        ),
    ]
