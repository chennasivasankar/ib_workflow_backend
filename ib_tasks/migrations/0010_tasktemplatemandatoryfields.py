# Generated by Django 2.2.1 on 2020-10-01 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ib_tasks', '0009_auto_20201001_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskTemplateMandatoryFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_display_name', models.CharField(default='Title', max_length=100)),
                ('title_placeholder_text', models.CharField(default='Title', max_length=100)),
                ('task_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.TaskTemplate')),
            ],
        ),
    ]