# Generated by Django 4.2.7 on 2023-11-26 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_info',
            new_name='order_infos',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_product',
            new_name='order_products',
        ),
    ]
