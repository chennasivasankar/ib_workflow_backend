# Generated by Django 2.2.1 on 2020-09-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ib_iam', '0006_auto_20200918_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAuthToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=36)),
                ('token', models.CharField(max_length=100)),
            ],
        ),
    ]
