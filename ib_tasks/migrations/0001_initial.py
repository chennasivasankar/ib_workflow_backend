# Generated by Django 2.2.1 on 2020-10-02 12:43

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
                ('field_type', models.CharField(choices=[('PLAIN_TEXT', 'PLAIN_TEXT'), ('PHONE_NUMBER', 'PHONE_NUMBER'), ('EMAIL', 'EMAIL'), ('URL', 'URL'), ('PASSWORD', 'PASSWORD'), ('NUMBER', 'NUMBER'), ('FLOAT', 'FLOAT'), ('LONG_TEXT', 'LONG_TEXT'), ('DROPDOWN', 'DROPDOWN'), ('GOF_SELECTOR', 'GOF_SELECTOR'), ('RADIO_GROUP', 'RADIO_GROUP'), ('CHECKBOX_GROUP', 'CHECKBOX_GROUP'), ('MULTI_SELECT_FIELD', 'MULTI_SELECT_FIELD'), ('MULTI_SELECT_LABELS', 'MULTI_SELECT_LABELS'), ('DATE', 'DATE'), ('TIME', 'TIME'), ('DATE_TIME', 'DATE_TIME'), ('IMAGE_UPLOADER', 'IMAGE_UPLOADER'), ('FILE_UPLOADER', 'FILE_UPLOADER'), ('SEARCHABLE', 'SEARCHABLE'), ('PLAIN_TEXT_CONTENT', 'PLAIN_TEXT_CONTENT'), ('HTML_CONTENT', 'HTML_CONTENT'), ('MARKDOWN_CONTENT', 'MARKDOWN_CONTENT')], max_length=100)),
                ('field_values', models.TextField(blank=True, null=True)),
                ('allowed_formats', models.TextField(blank=True, null=True)),
                ('help_text', models.CharField(blank=True, max_length=200, null=True)),
                ('tooltip', models.TextField(blank=True, null=True)),
                ('placeholder_text', models.CharField(blank=True, max_length=100, null=True)),
                ('error_messages', models.CharField(blank=True, max_length=200, null=True)),
                ('validation_regex', models.CharField(blank=True, max_length=200, null=True)),
                ('order', models.IntegerField()),
                ('is_unique', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=120)),
                ('project_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=120)),
                ('is_selected', models.CharField(choices=[('ENABLED', 'ENABLED'), ('DISABLED', 'DISABLED')], default='ENABLED', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GoF',
            fields=[
                ('gof_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('display_name', models.CharField(blank=True, max_length=50, null=True)),
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
                ('card_info_kanban', models.TextField()),
                ('card_info_list', models.TextField()),
                ('stage_color', models.CharField(max_length=100, null=True)),
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
                ('action_type', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('order', models.IntegerField(default=1)),
                ('py_function_import_path', models.TextField()),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Stage')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_update_datetime', models.DateTimeField(auto_now=True)),
                ('project_id', models.CharField(db_index=True, max_length=50)),
                ('task_display_id', models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True)),
                ('created_by', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('priority', models.CharField(blank=True, choices=[('HIGH', 'HIGH'), ('LOW', 'LOW'), ('MEDIUM', 'MEDIUM')], default='HIGH', max_length=20, null=True)),
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
            options={
                'unique_together': {('task', 'gof', 'same_gof_order')},
            },
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
                ('is_transition_template', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserTaskDelayReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_datetime', models.DateTimeField()),
                ('count', models.IntegerField()),
                ('reason_id', models.IntegerField()),
                ('reason', models.TextField(blank=True, null=True)),
                ('user_id', models.CharField(max_length=200)),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Stage')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Task')),
            ],
        ),
        migrations.CreateModel(
            name='TaskTemplateStatusVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variable', models.TextField()),
                ('value', models.TextField()),
                ('task_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.TaskTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='TaskTemplateMandatoryFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_display_name', models.CharField(default='Title', max_length=100)),
                ('title_placeholder_text', models.CharField(default='Title', max_length=100)),
                ('task_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.TaskTemplate')),
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
            name='TaskStageHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.CharField(blank=True, max_length=50, null=True)),
                ('assignee_id', models.CharField(blank=True, max_length=50, null=True)),
                ('joined_at', models.DateTimeField(auto_now=True, null=True)),
                ('left_at', models.DateTimeField(blank=True, null=True)),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Stage')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Task')),
            ],
        ),
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_json', models.TextField()),
                ('user_id', models.CharField(max_length=100)),
                ('acted_at', models.DateTimeField(auto_now_add=True)),
                ('action', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.StageAction')),
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
        migrations.AddField(
            model_name='task',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.TaskTemplate'),
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='parent_task', to='ib_tasks.Task')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_tasks', to='ib_tasks.Task')),
            ],
        ),
        migrations.CreateModel(
            name='StagePermittedRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.CharField(db_index=True, max_length=50)),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Stage')),
            ],
        ),
        migrations.CreateModel(
            name='StageGoF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.GoF')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Stage')),
            ],
        ),
        migrations.AddField(
            model_name='stageaction',
            name='transition_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.TaskTemplate'),
        ),
        migrations.AddField(
            model_name='stage',
            name='gof',
            field=models.ManyToManyField(through='ib_tasks.StageGoF', to='ib_tasks.GoF'),
        ),
        migrations.CreateModel(
            name='ProjectTaskTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=50)),
                ('task_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.TaskTemplate')),
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
            name='FilterCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(choices=[('GTE', 'GTE'), ('LTE', 'LTE'), ('GT', 'GT'), ('LT', 'LT'), ('NE', 'NE'), ('EQ', 'EQ'), ('CONTAINS', 'CONTAINS')], max_length=100)),
                ('value', models.TextField()),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Field')),
                ('filter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Filter')),
            ],
        ),
        migrations.AddField(
            model_name='filter',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.TaskTemplate'),
        ),
        migrations.CreateModel(
            name='FieldRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(db_index=True, max_length=50)),
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
            name='ElasticSearchTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elasticsearch_id', models.CharField(max_length=200, unique=True)),
                ('task_id', models.IntegerField(unique=True)),
            ],
            options={
                'unique_together': {('elasticsearch_id', 'task_id')},
            },
        ),
        migrations.CreateModel(
            name='CurrentTaskStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Stage')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Task')),
            ],
        ),
        migrations.CreateModel(
            name='ActionPermittedRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.CharField(db_index=True, max_length=50)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.StageAction')),
            ],
        ),
        migrations.CreateModel(
            name='TaskStageRp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rp_id', models.CharField(max_length=200)),
                ('added_at', models.DateTimeField(auto_now=True)),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Stage')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_tasks.Task')),
            ],
            options={
                'unique_together': {('task', 'stage', 'rp_id')},
            },
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
        migrations.AlterUniqueTogether(
            name='stageaction',
            unique_together={('stage', 'name')},
        ),
        migrations.AddIndex(
            model_name='gofrole',
            index=models.Index(fields=['role', 'permission_type'], name='ib_tasks_go_role_79f951_idx'),
        ),
        migrations.AddIndex(
            model_name='filter',
            index=models.Index(fields=['project_id', 'is_selected', 'created_by'], name='ib_tasks_fi_project_97e5eb_idx'),
        ),
        migrations.AddIndex(
            model_name='filter',
            index=models.Index(fields=['project_id', 'created_by'], name='ib_tasks_fi_project_7eb0ab_idx'),
        ),
        migrations.AddIndex(
            model_name='fieldrole',
            index=models.Index(fields=['role', 'permission_type'], name='ib_tasks_fi_role_a42d35_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='currenttaskstage',
            unique_together={('stage', 'task')},
        ),
    ]
