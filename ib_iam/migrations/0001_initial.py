# Generated by Django 2.2.1 on 2020-07-16 15:21

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
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.UUIDField(default=ib_iam.models.role.generate_uuid4, editable=False, primary_key=True, serialize=False)),
                ('role_id', models.CharField(max_length=1000, unique=True)),
                ('role_name', models.CharField(max_length=1000)),
                ('role_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.UUIDField(default=ib_iam.models.team.generate_uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
            ],
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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=1000)),
                ('is_admin', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_iam.Company')),
            ],
        ),
    ]
