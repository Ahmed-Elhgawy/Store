# Generated by Django 4.2.7 on 2023-11-26 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_orderinfo_cart_item_orderinfo_cart_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='cart_item',
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='cart_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.cartitem'),
        ),
    ]
