from django.db import models

from adotante.models import Adotante
from animal.models import Animal

# Create your models here.


class Adocao(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    adotante = models.ForeignKey(Adotante, on_delete=models.CASCADE)
    data_adocao = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.animal.nome} - {self.adotante.nome}"
