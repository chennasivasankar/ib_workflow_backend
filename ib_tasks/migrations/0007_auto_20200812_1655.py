# Generated by Django 2.2.1 on 2020-08-12 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ib_tasks', '0006_auto_20200811_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_display_id',
            field=models.CharField(default=None, max_length=50, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='TaskStageHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignee_id', models.CharField(blank=True, max_length=50, null=True)),
                ('joined_at', models.DateTimeField(auto_now=True, null=True)),
                ('left_at', models.DateTimeField(blank=True, null=True)),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Stage')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Task')),
            ],
        ),
    ]