# Generated by Django 3.2.11 on 2022-05-12 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0013_monthlyreportmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyreportmodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='monthlyReport/'),
        ),
    ]