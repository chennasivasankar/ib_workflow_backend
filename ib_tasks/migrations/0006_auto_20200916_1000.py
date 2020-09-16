# Generated by Django 2.2.1 on 2020-09-16 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ib_tasks', '0005_auto_20200907_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='StageGoF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.GoF')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Stage')),
            ],
        ),
        migrations.AddField(
            model_name='stage',
            name='gof',
            field=models.ManyToManyField(through='ib_tasks.StageGoF', to='ib_tasks.GoF'),
        ),
    ]
