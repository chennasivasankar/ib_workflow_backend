# Generated by Django 2.2.1 on 2020-10-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ib_tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='field_type',
            field=models.CharField(choices=[('PLAIN_TEXT', 'PLAIN_TEXT'), ('PHONE_NUMBER', 'PHONE_NUMBER'), ('EMAIL', 'EMAIL'), ('URL', 'URL'), ('PASSWORD', 'PASSWORD'), ('NUMBER', 'NUMBER'), ('FLOAT', 'FLOAT'), ('LONG_TEXT', 'LONG_TEXT'), ('DROPDOWN', 'DROPDOWN'), ('GOF_SELECTOR', 'GOF_SELECTOR'), ('RADIO_GROUP', 'RADIO_GROUP'), ('CHECKBOX_GROUP', 'CHECKBOX_GROUP'), ('MULTI_SELECT_FIELD', 'MULTI_SELECT_FIELD'), ('MULTI_SELECT_LABELS', 'MULTI_SELECT_LABELS'), ('DATE', 'DATE'), ('TIME', 'TIME'), ('DATE_TIME', 'DATE_TIME'), ('IMAGE_UPLOADER', 'IMAGE_UPLOADER'), ('FILE_UPLOADER', 'FILE_UPLOADER'), ('SEARCHABLE', 'SEARCHABLE'), ('PLAIN_TEXT_CONTENT', 'PLAIN_TEXT_CONTENT'), ('HTML_CONTENT', 'HTML_CONTENT'), ('MARKDOWN_CONTENT', 'MARKDOWN_CONTENT'), ('TEXT_SHARABLE_FIELD', 'TEXT_SHARABLE_FIELD')], max_length=100),
        ),
    ]
