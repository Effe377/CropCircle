# Generated by Django 5.1.3 on 2024-11-19 00:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='customerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
