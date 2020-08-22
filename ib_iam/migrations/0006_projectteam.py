# Generated by Django 2.2.1 on 2020-08-22 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ib_iam', '0005_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_iam.Project')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_iam.Team')),
            ],
            options={
                'unique_together': {('team', 'project')},
            },
        ),
    ]
