# Generated by Django 2.1.4 on 2019-01-26 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0004_offer_fuel'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='lat',
            field=models.DecimalField(decimal_places=13, default=0, max_digits=15),
        ),
        migrations.AddField(
            model_name='offer',
            name='long',
            field=models.DecimalField(decimal_places=13, default=0, max_digits=15),
        ),
    ]
