# Generated by Django 2.0.13 on 2019-05-15 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_product_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
