# Generated by Django 2.2.1 on 2020-08-08 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ib_tasks', '0004_auto_20200808_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stageaction',
            name='action_type',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]