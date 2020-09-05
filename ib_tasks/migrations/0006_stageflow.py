# Generated by Django 2.2.1 on 2020-09-05 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ib_tasks', '0005_auto_20200903_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='StageFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.StageAction')),
                ('next_stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Stage')),
                ('previous_stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='previous_stage', to='ib_tasks.Stage')),
            ],
        ),
    ]
