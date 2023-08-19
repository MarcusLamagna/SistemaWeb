from django.db import models


# Create your models here.

class Endereco(models.Model):
    logradouro = models.CharField(max_length=255, blank=False, null=False)
    bairro = models.CharField(max_length=255, blank=False, null=False)
    cidade = models.CharField(max_length=255, blank=False, null=False)
    numero = models.IntegerField(blank=False, null=False)
    cep = models.CharField(max_length=10, blank=False, null=False)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.logradouro
