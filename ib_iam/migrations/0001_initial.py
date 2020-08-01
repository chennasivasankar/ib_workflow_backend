# Generated by Django 2.2.1 on 2020-08-01 09:24

from django.db import migrations, models
import django.db.models.deletion
import ib_iam.models.company
import ib_iam.models.role
import ib_iam.models.team


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.UUIDField(default=ib_iam.models.company.generate_uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('logo_url', models.URLField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_update_datetime', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=ib_iam.models.role.generate_uuid4, editable=False, primary_key=True, serialize=False)),
                ('role_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_update_datetime', models.DateTimeField(auto_now=True)),
                ('team_id', models.UUIDField(default=ib_iam.models.team.generate_uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_by', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=1000)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_iam.Team')),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=1000)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_iam.Role')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=1000)),
                ('is_admin', models.BooleanField(default=False)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='ib_iam.Company')),
            ],
        ),
    ]
