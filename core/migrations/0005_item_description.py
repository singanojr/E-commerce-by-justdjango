# Generated by Django 3.1.1 on 2020-09-11 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='this is a test desciption hello world~~~~~~~~~~~~~~~~'),
            preserve_default=False,
        ),
    ]
