# Generated by Django 2.2.1 on 2020-08-22 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ib_tasks', '0002_auto_20200813_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project_id',
            field=models.CharField(default='unknown_project', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskstagehistory',
            name='team_id',
            field=models.CharField(default='unknown_team', max_length=50),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ProjectTaskTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=50)),
                ('task_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.TaskTemplate')),
            ],
        ),
    ]
