# Generated by Django 2.0.6 on 2021-08-25 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0005_auto_20210825_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('pk_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=20)),
                ('apellido_cliente', models.CharField(max_length=20)),
                ('dpi', models.CharField(max_length=12)),
                ('telefono', models.CharField(max_length=8)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='envio',
            fields=[
                ('pk_envio', models.AutoField(primary_key=True, serialize=False)),
                ('direccion_envio', models.CharField(max_length=80)),
                ('fecha_envio', models.DateField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
                ('fk_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('pk_producto', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='vendedor',
            fields=[
                ('pk_vendedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_vendedor', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=8)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='fk_customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='fk_product',
        ),
        migrations.DeleteModel(
            name='seller',
        ),
        migrations.DeleteModel(
            name='customer',
        ),
        migrations.DeleteModel(
            name='order',
        ),
        migrations.DeleteModel(
            name='product',
        ),
        migrations.AddField(
            model_name='envio',
            name='fk_producto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='storage.producto'),
        ),
    ]