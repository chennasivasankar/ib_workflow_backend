# Generated by Django 2.2.1 on 2020-07-21 16:00

from django.db import migrations, models
import ib_iam.models.role


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_update_datetime', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=ib_iam.models.role.generate_uuid4, editable=False, primary_key=True, serialize=False)),
                ('role_id', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
