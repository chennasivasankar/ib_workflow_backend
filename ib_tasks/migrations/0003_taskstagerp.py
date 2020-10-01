# Generated by Django 2.2.1 on 2020-08-27 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ib_tasks', '0002_field_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStageRp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rp_id', models.CharField(max_length=200)),
                ('added_at', models.DateTimeField(auto_now=True)),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Stage')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Task')),
            ],
        ),
    ]
