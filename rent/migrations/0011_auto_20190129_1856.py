# Generated by Django 2.1.4 on 2019-01-29 17:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0010_auto_20190129_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='id',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='id',
        ),
        migrations.AddField(
            model_name='car',
            name='carUUID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='offer',
            name='offerUUID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]