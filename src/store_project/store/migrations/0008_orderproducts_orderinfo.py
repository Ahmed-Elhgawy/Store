# Generated by Django 4.2.7 on 2023-11-26 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_delete_orderinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('name', models.CharField(max_length=20)),
                ('cardnumber', models.CharField(max_length=20)),
                ('expirationdate', models.CharField(max_length=5)),
                ('securitycode', models.CharField(max_length=3)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.orderproducts')),
            ],
        ),
    ]