from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ib_iam', '0005_auto_20200908_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]