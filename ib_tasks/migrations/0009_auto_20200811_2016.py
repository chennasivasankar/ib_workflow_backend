# Generated by Django 2.2.1 on 2020-08-11 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ib_tasks', '0008_auto_20200811_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_display_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
