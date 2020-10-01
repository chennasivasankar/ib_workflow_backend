# Generated by Django 2.2.1 on 2020-10-01 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ib_tasks', '0008_auto_20200929_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='stageaction',
            name='order',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='field',
            name='field_type',
            field=models.CharField(choices=[('PLAIN_TEXT', 'PLAIN_TEXT'), ('PHONE_NUMBER', 'PHONE_NUMBER'), ('EMAIL', 'EMAIL'), ('URL', 'URL'), ('PASSWORD', 'PASSWORD'), ('NUMBER', 'NUMBER'), ('FLOAT', 'FLOAT'), ('LONG_TEXT', 'LONG_TEXT'), ('DROPDOWN', 'DROPDOWN'), ('GOF_SELECTOR', 'GOF_SELECTOR'), ('RADIO_GROUP', 'RADIO_GROUP'), ('CHECKBOX_GROUP', 'CHECKBOX_GROUP'), ('MULTI_SELECT_FIELD', 'MULTI_SELECT_FIELD'), ('MULTI_SELECT_LABELS', 'MULTI_SELECT_LABELS'), ('DATE', 'DATE'), ('TIME', 'TIME'), ('DATE_TIME', 'DATE_TIME'), ('IMAGE_UPLOADER', 'IMAGE_UPLOADER'), ('FILE_UPLOADER', 'FILE_UPLOADER'), ('SEARCHABLE', 'SEARCHABLE'), ('PLAIN_TEXT_CONTENT', 'PLAIN_TEXT_CONTENT'), ('HTML_CONTENT', 'HTML_CONTENT'), ('MARKDOWN_CONTENT', 'MARKDOWN_CONTENT')], max_length=100),
        ),
        migrations.AlterField(
            model_name='gof',
            name='display_name',
            field=models.CharField(blank=True, max_length=50, null=True),
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
    ]
