from email.policy import default
from django.db import models

# Create your models here.

class tb_usuario(models.Model):
    usu_nombre = models.CharField(max_length=30)
    usu_password = models.CharField(max_length=40)
    usu_rol = models.CharField(max_length=10)

class tb_familia(models.Model):
    fam_usu_id = models.IntegerField()

class db_dispensa(models.Model):
    dis_fam_id = models.IntegerField()

class tb_producto(models.Model):
    pro_nombre = models.CharField(max_length=20)
    pro_cantidad = models.IntegerField()
    pro_dis_id = models.IntegerField()

class tb_datos_producto(models.Model):
    dat_precio = models.IntegerField()
    dat_caducidad = models.DateField()
    dat_gasto = models.IntegerField()
    dat_pro_id = models.IntegerField()
