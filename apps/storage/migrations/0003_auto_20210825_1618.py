# Generated by Django 2.0.6 on 2021-08-25 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20210825_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='fk_seller',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]