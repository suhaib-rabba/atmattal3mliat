# Generated by Django 3.2.11 on 2022-03-27 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_rename_apps_applications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Combustibles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dieselTamem_2019', models.FileField(upload_to='combustibles/diesel/')),
                ('dieselTamem_2020', models.FileField(upload_to='combustibles/diesel/')),
                ('dieselTamem_2021', models.FileField(upload_to='combustibles/diesel/')),
                ('dieselTamem_2022', models.FileField(upload_to='combustibles/diesel/')),
            ],
        ),
    ]
