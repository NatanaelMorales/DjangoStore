# Generated by Django 2.0.6 on 2021-09-23 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0014_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mensaje',
            field=models.TextField(),
        ),
    ]
