# Generated by Django 4.2.7 on 2023-11-26 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_rename_order_info_order_order_infos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
