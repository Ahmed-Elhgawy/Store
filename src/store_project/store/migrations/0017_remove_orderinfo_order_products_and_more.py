# Generated by Django 4.2.7 on 2023-11-27 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_remove_orderproducts_user_orderinfo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='order_products',
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='order_products',
            field=models.ManyToManyField(null=True, to='store.orderproducts'),
        ),
    ]