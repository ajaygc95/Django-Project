# Generated by Django 2.2 on 2019-12-19 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newcart', '0003_remove_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
