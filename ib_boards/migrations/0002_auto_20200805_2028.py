# Generated by Django 2.2.1 on 2020-08-05 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ib_boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userstarredboard',
            unique_together={('user_id', 'board')},
        ),
    ]