# Generated by Django 2.2.1 on 2020-08-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ib_iam', '0005_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
