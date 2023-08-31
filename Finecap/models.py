from django.db import models



class Stand(models.Model):
    localizacão = models.CharField(max_length=255)
    valor = models.DecimalField(decimal_places=2,max_digits=8)
    

class Reserva(models.Model): 
    cnpj = models.CharField(max_length=255)
    nome_empresa = models.CharField(max_length=255)
    categoria_empresa = models.CharField(max_length=255)
    quitado = models.BooleanField()
    reserva = models.OneToOneField(Stand, on_delete=models.CASCADE)