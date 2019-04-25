# Generated by Django 2.0.13 on 2019-04-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20190425_1506'),
        ('cart', '0003_auto_20190425_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(blank=True, to='product.Product'),
        ),
    ]