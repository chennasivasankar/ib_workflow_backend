# Generated by Django 2.2.1 on 2020-10-02 12:43

from django.db import migrations, models
import django.db.models.deletion
import ib_utility_tools.models.checklist
import ib_utility_tools.models.checklist_item
import ib_utility_tools.models.timer


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('checklist_id', models.UUIDField(default=ib_utility_tools.models.checklist.generate_uuid, editable=False, primary_key=True, serialize=False)),
                ('entity_id', models.CharField(max_length=200)),
                ('entity_type', models.CharField(max_length=25, validators=[ib_utility_tools.models.checklist.validate_entity_type])),
            ],
            options={
                'unique_together': {('entity_id', 'entity_type')},
            },
        ),
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('timer_id', models.UUIDField(default=ib_utility_tools.models.timer.generate_uuid, editable=False, primary_key=True, serialize=False)),
                ('entity_id', models.CharField(max_length=200)),
                ('entity_type', models.CharField(max_length=25, validators=[ib_utility_tools.models.timer.validate_timer_entity_type])),
                ('start_datetime', models.DateTimeField(null=True)),
                ('duration_in_seconds', models.IntegerField(default=0)),
                ('is_running', models.BooleanField(default=False)),
            ],
            options={
                'unique_together': {('entity_id', 'entity_type')},
            },
        ),
        migrations.CreateModel(
            name='ChecklistItem',
            fields=[
                ('checklist_item_id', models.UUIDField(default=ib_utility_tools.models.checklist_item.generate_uuid, editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('is_checked', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=ib_utility_tools.models.checklist_item.get_datetime_now)),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checklist_items', to='ib_utility_tools.Checklist')),
            ],
        ),
    ]
