# Generated by Django 3.2.11 on 2022-04-06 11:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_auto_20220327_0337'),
    ]

    operations = [
        migrations.CreateModel(
            name='date_app',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_now', models.DateField(default=datetime.date(2022, 4, 6))),
            ],
        ),
    ]
