# Generated by Django 2.1.4 on 2019-01-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0007_auto_20190126_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='carId',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='offerId',
        ),
        migrations.AddField(
            model_name='car',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
