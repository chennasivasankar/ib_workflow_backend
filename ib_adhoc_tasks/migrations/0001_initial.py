# Generated by Django 2.2.1 on 2020-09-22 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupByInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('group_by', models.CharField(max_length=50)),
                ('order', models.IntegerField()),
                ('view_type', models.CharField(choices=[('LIST', 'LIST'), ('KANBAN', 'KANBAN')], max_length=20)),
            ],
        ),
    ]