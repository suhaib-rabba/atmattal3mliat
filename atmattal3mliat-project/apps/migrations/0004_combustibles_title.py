# Generated by Django 3.2.11 on 2022-03-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_combustibles'),
    ]

    operations = [
        migrations.AddField(
            model_name='combustibles',
            name='title',
            field=models.CharField(default='diesel', max_length=255),
            preserve_default=False,
        ),
    ]
