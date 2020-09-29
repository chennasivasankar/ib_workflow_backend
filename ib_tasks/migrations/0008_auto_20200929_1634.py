# Generated by Django 2.2.1 on 2020-09-29 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ib_tasks', '0007_subtask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldrole',
            name='role',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='filter',
            name='project_id',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='project_id',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_display_id',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddIndex(
            model_name='fieldrole',
            index=models.Index(fields=['role', 'permission_type'], name='ib_tasks_fi_role_a42d35_idx'),
        ),
        migrations.AddIndex(
            model_name='filter',
            index=models.Index(fields=['project_id', 'is_selected'], name='ib_tasks_fi_project_9d3349_idx'),
        ),
    ]
