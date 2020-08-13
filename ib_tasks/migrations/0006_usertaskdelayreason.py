# Generated by Django 2.2.1 on 2020-08-11 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ib_tasks', '0005_auto_20200808_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTaskDelayReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_datetime', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField()),
                ('reason_id', models.IntegerField()),
                ('reason', models.TextField(blank=True, null=True)),
                ('user_id', models.CharField(max_length=200)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Task')),
            ],
        ),
    ]
