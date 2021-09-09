from django.db import models

# Create your models here.

class cliente(models.Model):
    pk_cliente = models.AutoField(primary_key=True, null=False, blank=False)
    nombre_cliente = models.CharField(max_length=20, null=False, blank=False)
    apellido_cliente = models.CharField(max_length=20, null=False, blank=False)
    dpi = models.CharField(max_length=12, null=False, blank=False)
    telefono = models.CharField(max_length=8, null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)

class vendedor(models.Model):
    pk_vendedor = models.AutoField(primary_key=True, null=False, blank=False)
    nombre_vendedor = models.CharField(max_length=20, null=False, blank=False)
    telefono = models.CharField(max_length=8, null=False, blank=False)
    dpi = models.CharField(max_length=12, null=False, blank=False)

class producto(models.Model):
    pk_producto = models.AutoField(primary_key=True, null=False, blank=False)
    codigo = models.CharField(max_length=9, null=False, blank=False)
    nombre = models.CharField(max_length=40, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    imagen1 = models.URLField(max_length=800, default='https://i.postimg.cc/Y0gkNhTM/3aabe0e9a520b9ad90407a82f85adb42.jpg', null=False, blank=False)
    precio = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2)

class envio(models.Model):
    pk_envio = models.AutoField(primary_key=True, null=False, blank=False)
    fk_cliente = models.ForeignKey(cliente, null=False, blank=False, on_delete=models.CASCADE)
    direccion_envio = models.CharField(max_length=80, null=False, blank=False)
    fecha_envio = models.DateField(auto_now=False, auto_now_add=True, null=False, blank=False)
    cantidad = models.IntegerField(null=False, blank=False)
    fk_producto = models.OneToOneField(producto, null=False, blank=False, on_delete=models.CASCADE)

