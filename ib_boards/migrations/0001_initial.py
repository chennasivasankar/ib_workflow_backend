# Generated by Django 2.2.1 on 2020-07-24 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('board_id', models.CharField(max_length=200, primary_key=True,
                                              serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('column_id',
                 models.CharField(max_length=200, primary_key=True,
                                  serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('display_order', models.IntegerField()),
                ('task_selection_config', models.TextField(null=True)),
                ('kanban_brief_view_config', models.TextField(null=True)),
                ('list_brief_view_config', models.TextField(null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('board',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='ib_boards.Board')),
            ],
        ),
        migrations.CreateModel(
            name='ColumnPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('user_role_id', models.CharField(max_length=200)),
                ('column',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='ib_boards.Column')),
            ],
        ),
    ]
