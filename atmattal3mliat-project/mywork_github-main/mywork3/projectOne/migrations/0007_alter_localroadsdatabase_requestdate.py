# Generated by Django 3.2.3 on 2021-06-06 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectOne', '0006_auto_20210606_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localroadsdatabase',
            name='requestDate',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]