# Generated by Django 4.2.4 on 2023-08-24 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hwapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='products',
            new_name='product',
        ),
    ]
