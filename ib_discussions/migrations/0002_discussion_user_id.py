# Generated by Django 2.2.1 on 2020-07-22 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ib_discussions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='user_id',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]