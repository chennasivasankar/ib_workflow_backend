# Generated by Django 2.2.1 on 2020-08-26 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ib_iam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectrole',
            name='description',
            field=models.TextField(blank=True, max_length=120, null=True),
        ),
    ]
