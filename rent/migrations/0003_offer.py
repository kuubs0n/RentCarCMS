# Generated by Django 2.1.4 on 2019-01-26 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_car_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rent.Car')),
            ],
        ),
    ]