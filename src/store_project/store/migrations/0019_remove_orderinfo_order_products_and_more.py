# Generated by Django 4.2.7 on 2023-11-27 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_alter_orderinfo_order_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='order_products',
        ),
        migrations.RemoveField(
            model_name='orderinfo',
            name='user',
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='products',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='OrderProducts',
        ),
    ]
