# Generated by Django 2.1.4 on 2019-02-05 22:12

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0018_auto_20190205_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Content'),
        ),
    ]
