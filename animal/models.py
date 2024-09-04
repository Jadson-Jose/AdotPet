from django.db import models

from abrigo.models import Abrigo

# Create your models here.


class Animal(models.Model):

    TIPOS = [
        ('C', 'Cachorro'),
        ('G', 'Gato'),
        ('P', 'Pássaro'),
        ('R', 'Roedor'),
        ('O', 'Outros'),
    ]

    PORTES = [
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    ]

    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)  # Exemplo: Gato, Cachorro
    raca = models.CharField(max_length=50, blank=True, null=True)
    idade = models.IntegerField()  # em anos
    porte = models.CharField(max_length=20)  # Exemplo: Pequeno, Médio, Grande
    cor = models.CharField(max_length=30, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='fotos_animais/', blank=True, null=True)
    data_resgate = models.DateField(auto_now_add=True)
    adotado = models.BooleanField(default=False)
    abrigo = models.ForeignKey(
        Abrigo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.nome
