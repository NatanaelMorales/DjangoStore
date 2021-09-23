# Generated by Django 2.0.6 on 2021-09-23 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0012_auto_20210908_1050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['nombre_cliente'], 'verbose_name': 'cliente', 'verbose_name_plural': 'clientes'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['nombre'], 'verbose_name': 'producto', 'verbose_name_plural': 'productos'},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen1',
            field=models.URLField(default='https://i.postimg.cc/Y0gkNhTM/3aabe0e9a520b9ad90407a82f85adb42.jpg', max_length=800),
        ),
    ]