# Generated by Django 2.2.1 on 2020-08-10 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ib_tasks', '0005_auto_20200808_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskReasons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_choice', models.TextField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Task')),
            ],
        ),
        migrations.CreateModel(
            name='TaskDueDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_datetime', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField()),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.TaskReasons')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Task')),
            ],
        ),
    ]
