# Generated by Django 2.2 on 2019-12-19 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0013_detail_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='price',
            field=models.FloatField(),
        ),
    ]
