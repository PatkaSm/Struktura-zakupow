# Generated by Django 2.0.13 on 2019-05-07 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20190507_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='caterogry',
            new_name='category',
        ),
    ]