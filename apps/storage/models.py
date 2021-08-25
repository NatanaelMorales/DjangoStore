from django.db import models

# Create your models here.

class customer(models.Model): #cliente
    pk_id_customer = models.AutoField(primary_key=True, null=False, blank=False)
    name_client = models.CharField(max_length=20, null=False, blank=False)
    surname_client = models.CharField(max_length=20, null=False, blank=False)
    dpi = models.CharField(max_length=12, null=False, blank=False)
    telephone = models.CharField(max_length=8, null=False, blank=False)
    direction = models.CharField(max_length=50, null=False, blank=False)

class seller(models.Model): #vendedor
    pk_id_seller = models.AutoField(primary_key=True, null=False, blank=False)
    name_seller = models.CharField(max_length=20, null=False, blank=False)
    telephone = models.CharField(max_length=8, null=False, blank=False)

class order(models.Model): #envio
    pk_num_order = models.AutoField(primary_key=True, null=False, blank=False)
    fk_customer = models.ForeignKey(customer, null=False, blank=False, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=80, null=False, blank=False)
    send_date = models.DateField(auto_now=False, auto_now_add=True, null=False, blank=False)
    amount = models.IntegerField(null=False, blank=False)
    fk_seller = models.OneToOneField(seller, null=False, blank=False, on_delete=models.CASCADE)

class product(models.Model): #producto
    pk_product = models.AutoField(primary_key=True, null=False, blank=False)
    code = models.CharField(max_length=8, null=False, blank=False)
    name = models.CharField(max_length=40, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(null=False, blank=False, max_digits=4, decimal_places=2)

