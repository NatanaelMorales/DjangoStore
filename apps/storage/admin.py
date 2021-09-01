from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

# -------------------------------------
class ResourceProducto(resources.ModelResource):
    class Meta:
        model = producto

class AdminProducto(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['pk_producto', 'codigo', 'nombre', 'descripcion', 'precio']
    resource_class = ResourceProducto

admin.site.register(producto, AdminProducto)

# -------------------------------------
class ResourceCliente(resources.ModelResource):
    class Meta:
        model = cliente

class AdminCliente(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['dpi']
    list_display = ['pk_cliente', 'nombre_cliente', 'apellido_cliente', 'dpi', 'telefono', 'direccion']
    resource_class = ResourceCliente

admin.site.register(cliente, AdminCliente)

# -------------------------------------
class ResourceVendedor(resources.ModelResource):
    class Meta:
        model = vendedor

class AdminVendedor(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre_vendedor']
    list_display = ['pk_vendedor', 'nombre_vendedor', 'telefono', 'dpi']
    resource_class = ResourceVendedor

admin.site.register(vendedor, AdminVendedor)

# -------------------------------------
class ResourceEnvio(resources.ModelResource):
    class Meta:
        model = envio

class AdminEnvio(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['pk_envio']
    list_display = ['pk_envio', 'fk_cliente', 'direccion_envio', 'fecha_envio', 'cantidad', 'fk_producto']
    resource_class = ResourceEnvio

admin.site.register(envio, AdminEnvio)