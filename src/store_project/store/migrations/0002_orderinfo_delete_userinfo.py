# Generated by Django 4.2.7 on 2023-11-26 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.cart')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.useraddress')),
                ('user_visa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.uservisa')),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
