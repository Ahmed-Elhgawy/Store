# Generated by Django 4.2.7 on 2023-11-26 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_orderinfo_cart_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='cart_item',
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='cart_item',
            field=models.ManyToManyField(to='store.cartitem'),
        ),
    ]
