# Generated by Django 4.2.7 on 2023-11-26 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='order_products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.orderproducts'),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]