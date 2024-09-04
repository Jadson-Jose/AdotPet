from django.db import models

# Create your models here.


class Abrigo(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    telelfone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nome
