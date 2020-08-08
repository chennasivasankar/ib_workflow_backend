# Generated by Django 2.2.1 on 2020-08-08 15:34

from django.db import migrations, models
import django.db.models.deletion
import ib_discussions.models.comment
import ib_discussions.models.discussion
import ib_discussions.models.discussion_set
import ib_discussions.models.entity
import ib_discussions.models.multimedia


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=ib_discussions.models.comment.generate_uuid, editable=False, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(default=ib_discussions.models.comment.get_datetime_now)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.UUIDField(default=ib_discussions.models.entity.generate_uuid, editable=False, primary_key=True, serialize=False)),
                ('entity_type', models.CharField(choices=[('TASK', 'TASK')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MultiMedia',
            fields=[
                ('id', models.UUIDField(default=ib_discussions.models.multimedia.generate_uuid, editable=False, primary_key=True, serialize=False)),
                ('format_type', models.CharField(choices=[('IMAGE', 'IMAGE'), ('VIDEO', 'VIDEO')], max_length=30)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionSet',
            fields=[
                ('id', models.UUIDField(default=ib_discussions.models.discussion_set.generate_uuid, editable=False, primary_key=True, serialize=False)),
                ('entity_id', models.CharField(max_length=200)),
                ('entity_type', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('entity_id', 'entity_type')},
            },
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.UUIDField(default=ib_discussions.models.discussion.generate_uuid, editable=False, primary_key=True, serialize=False)),
                ('user_id', models.UUIDField(editable=False)),
                ('description', models.TextField()),
                ('title', models.TextField()),
                ('created_at', models.DateTimeField(default=ib_discussions.models.discussion.get_datetime_now)),
                ('is_clarified', models.BooleanField(default=False)),
                ('discussion_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_discussions.DiscussionSet')),
            ],
        ),
        migrations.CreateModel(
            name='CommentWithMultiMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_discussions.Comment')),
                ('multimedia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_discussions.MultiMedia')),
            ],
        ),
        migrations.CreateModel(
            name='CommentWithMentionUserId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mention_user_id', models.CharField(max_length=40)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ib_discussions.Comment')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='discussion',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ib_discussions.Discussion'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='ib_discussions.Comment'),
        ),
    ]
