# Generated by Django 2.2.1 on 2020-09-07 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ib_tasks', '0005_auto_20200903_1737'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='taskstagerp',
            unique_together={('task', 'stage', 'rp_id')},
        ),
        migrations.CreateModel(
            name='StageFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.StageAction')),
                ('next_stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Stage')),
                ('previous_stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_stages', to='ib_tasks.Stage')),
            ],
            options={
                'unique_together': {('previous_stage', 'action', 'next_stage')},
            },
        ),
    ]
