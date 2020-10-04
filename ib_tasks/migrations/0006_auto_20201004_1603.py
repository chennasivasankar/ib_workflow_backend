# Generated by Django 2.2.1 on 2020-10-04 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ib_tasks', '0005_auto_20201004_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='transitiontemplatetasks',
            name='transition_task',
            field=models.ForeignKey(null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to='ib_tasks.Task'),
        ),
        migrations.AlterField(
            model_name='transitiontemplatetasks',
            name='task',
            field=models.ForeignKey(null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='transition_tasks',
                                    to='ib_tasks.Task'),
        ),
    ]
