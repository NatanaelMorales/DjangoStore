# Generated by Django 2.0.6 on 2021-08-25 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_auto_20210825_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='fk_customer',
        ),
        migrations.DeleteModel(
            name='order',
        ),
    ]
