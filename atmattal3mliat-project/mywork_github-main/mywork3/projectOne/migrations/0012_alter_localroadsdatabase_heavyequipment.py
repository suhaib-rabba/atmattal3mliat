# Generated by Django 3.2.3 on 2021-06-13 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectOne', '0011_auto_20210608_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localroadsdatabase',
            name='heavyEquipment',
            field=models.CharField(blank=True, choices=[('لودر', 'لودر'), ('جك همر', 'جك همر'), ('قلاب', 'قلاب'), ('جريدير', 'جريدر'), ('مدحلة + تنك مياه', 'مدحلة + تنك مياه')], max_length=200, null=True),
        ),
    ]
