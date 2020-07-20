# Generated by Django 2.2.1 on 2020-07-20 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('field_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('display_name', models.CharField(max_length=100)),
                ('required', models.BooleanField(default=True)),
                ('field_type', models.CharField(choices=[('PLAIN_TEXT', 'PLAIN_TEXT'), ('PHONE_NUMBER', 'PHONE_NUMBER'), ('EMAIL', 'EMAIL'), ('URL', 'URL'), ('PASSWORD', 'PASSWORD'), ('NUMBER', 'NUMBER'), ('FLOAT', 'FLOAT'), ('LONG_TEXT', 'LONG_TEXT'), ('DROPDOWN', 'DROPDOWN'), ('<GOF_SELECTOR>', '<GOF_SELECTOR>')], max_length=100)),
                ('field_values', models.TextField(null=True)),
                ('allowed_formats', models.TextField(null=True)),
                ('help_text', models.CharField(max_length=200, null=True)),
                ('tooltip', models.TextField(null=True)),
                ('placeholder_text', models.CharField(max_length=100, null=True)),
                ('error_messages', models.CharField(max_length=200, null=True)),
                ('validation_regex', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoF',
            fields=[
                ('gof_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('display_name', models.CharField(max_length=50)),
                ('max_columns', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='TaskTemplate',
            fields=[
                ('template_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GoFRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('permission_type', models.CharField(choices=[('WRITE', 'WRITE'), ('READ', 'READ')], max_length=100)),
                ('gof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.GoF')),
            ],
        ),
        migrations.AddField(
            model_name='gof',
            name='task_template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.TaskTemplate'),
        ),
        migrations.CreateModel(
            name='GlobalConstant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.IntegerField()),
                ('task_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='global_constants', to='ib_tasks.TaskTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='FieldRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('permission_type', models.CharField(choices=[('WRITE', 'WRITE'), ('READ', 'READ')], max_length=100)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Field')),
            ],
        ),
        migrations.AddField(
            model_name='field',
            name='gof',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.GoF'),
        ),
    ]
