# Generated by Django 2.2.5 on 2021-08-22 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectOne', '0018_auto_20210822_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localroadsdatabase',
            name='land_chart',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
