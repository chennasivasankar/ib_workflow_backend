# Generated by Django 2.2.1 on 2020-08-24 11:27

from django.db import migrations, models
import django.db.models.deletion
import ib_iam.models.project_role


class Migration(migrations.Migration):

    dependencies = [
        ('ib_iam', '0007_projectteam'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectRole',
            fields=[
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_update_datetime', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=ib_iam.models.project_role.generate_uuid4, editable=False, primary_key=True, serialize=False)),
                ('role_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=120)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_iam.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='userrole',
            name='role',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.AddField(
            model_name='userrole',
            name='project_role',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ib_iam.ProjectRole'),
            preserve_default=False,
        ),
    ]
