# Generated by Django 3.2.11 on 2022-04-13 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0010_auto_20220412_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date_app',
            name='maintenance_interval',
            field=models.IntegerField(),
        ),
    ]
