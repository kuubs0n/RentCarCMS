# Generated by Django 2.1.4 on 2019-02-05 22:01

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0016_auto_20190205_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
