# Generated by Django 4.0.1 on 2022-05-07 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_order_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='Order',
            new_name='order',
        ),
    ]
