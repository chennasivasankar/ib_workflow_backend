# Generated by Django 2.2.1 on 2020-08-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ib_tasks', '0002_auto_20200807_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='is_selected',
            field=models.CharField(choices=[('ENABLED', 'ENABLED'), ('DISABLED', 'DISABLED')], default='ENABLED', max_length=100),
        ),
    ]
