# Generated by Django 2.1.4 on 2019-02-05 22:21

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0019_auto_20190205_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
