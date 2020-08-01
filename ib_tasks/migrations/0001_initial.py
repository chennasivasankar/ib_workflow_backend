# Generated by Django 2.2.1 on 2020-07-31 16:24

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
                ('field_type', models.CharField(choices=[('PLAIN_TEXT', 'PLAIN_TEXT'), ('PHONE_NUMBER', 'PHONE_NUMBER'), ('EMAIL', 'EMAIL'), ('URL', 'URL'), ('PASSWORD', 'PASSWORD'), ('NUMBER', 'NUMBER'), ('FLOAT', 'FLOAT'), ('LONG_TEXT', 'LONG_TEXT'), ('DROPDOWN', 'DROPDOWN'), ('GOF_SELECTOR', 'GOF_SELECTOR'), ('RADIO_GROUP', 'RADIO_GROUP'), ('CHECKBOX_GROUP', 'CHECKBOX_GROUP'), ('MULTI_SELECT_FIELD', 'MULTI_SELECT_FIELD'), ('MULTI_SELECT_LABELS', 'MULTI_SELECT_LABELS'), ('DATE', 'DATE'), ('TIME', 'TIME'), ('DATE_TIME', 'DATE_TIME'), ('IMAGE_UPLOADER', 'IMAGE_UPLOADER'), ('FILE_UPLOADER', 'FILE_UPLOADER'), ('SEARCHABLE', 'SEARCHABLE')], max_length=100)),
                ('field_values', models.TextField(blank=True, null=True)),
                ('allowed_formats', models.TextField(blank=True, null=True)),
                ('help_text', models.CharField(blank=True, max_length=200, null=True)),
                ('tooltip', models.TextField(blank=True, null=True)),
                ('placeholder_text', models.CharField(blank=True, max_length=100, null=True)),
                ('error_messages', models.CharField(blank=True, max_length=200, null=True)),
                ('validation_regex', models.CharField(blank=True, max_length=200, null=True)),
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
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_id', models.CharField(max_length=200, unique=True)),
                ('task_template_id', models.CharField(max_length=200)),
                ('display_name', models.TextField()),
                ('value', models.IntegerField()),
                ('display_logic', models.TextField()),
                ('field_display_config', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_update_datetime', models.DateTimeField(auto_now=True)),
                ('template_id', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskGoF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('same_gof_order', models.IntegerField()),
                ('gof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.GoF')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Task')),
            ],
        ),
        migrations.CreateModel(
            name='TaskStatusVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=120)),
                ('variable', models.CharField(max_length=120)),
                ('value', models.CharField(max_length=120)),
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
            name='TaskTemplateGlobalConstants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_template_id', models.IntegerField()),
                ('variable', models.CharField(max_length=100, unique=True)),
                ('value', models.CharField(max_length=100)),
                ('data_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TaskTemplateStatusVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_template_id', models.CharField(max_length=200)),
                ('variable', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskTemplateStatusVariables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_template_id', models.IntegerField()),
                ('variable', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TaskTemplateInitialStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Stage')),
                ('task_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.TaskTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='TaskTemplateGoFs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('enable_add_another_gof', models.BooleanField(default=False)),
                ('gof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.GoF')),
                ('task_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.TaskTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_json', models.TextField()),
                ('user_id', models.IntegerField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Task')),
            ],
        ),
        migrations.CreateModel(
            name='TaskGoFField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_response', models.TextField()),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Field')),
                ('task_gof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.TaskGoF')),
            ],
        ),
        migrations.CreateModel(
            name='StageAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('button_text', models.TextField()),
                ('button_color', models.TextField(null=True)),
                ('logic', models.TextField()),
                ('py_function_import_path', models.TextField()),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Stage')),
            ],
            options={
                'unique_together': {('stage', 'name')},
            },
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
            field=models.ManyToManyField(through='ib_tasks.TaskTemplateGoFs', to='ib_tasks.TaskTemplate'),
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
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.GoF'),
        ),
        migrations.CreateModel(
            name='ActionPermittedRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.CharField(max_length=200)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.StageAction')),
            ],
        ),
        migrations.CreateModel(
            name='TaskStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Stage')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Task')),
            ],
            options={
                'unique_together': {('stage', 'task')},
            },
        ),
    ]
