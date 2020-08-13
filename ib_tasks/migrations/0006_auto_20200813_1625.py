# Generated by Django 2.2.1 on 2020-08-13 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ib_tasks', '0005_auto_20200808_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentTaskStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Stage')),
            ],
        ),
        migrations.CreateModel(
            name='TaskStageHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignee_id', models.CharField(blank=True, max_length=50, null=True)),
                ('joined_at', models.DateTimeField(auto_now=True, null=True)),
                ('left_at', models.DateTimeField(blank=True, null=True)),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Stage')),
            ],
        ),
        migrations.CreateModel(
            name='UserTaskDelayReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_datetime', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField()),
                ('reason_id', models.IntegerField()),
                ('reason', models.TextField(blank=True, null=True)),
                ('user_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='task_display_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='TaskStage',
        ),
        migrations.AddField(
            model_name='usertaskdelayreason',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Task'),
        ),
        migrations.AddField(
            model_name='taskstagehistory',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Task'),
        ),
        migrations.AddField(
            model_name='currenttaskstage',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Task'),
        ),
        migrations.AlterUniqueTogether(
            name='currenttaskstage',
            unique_together={('stage', 'task')},
        ),
    ]
