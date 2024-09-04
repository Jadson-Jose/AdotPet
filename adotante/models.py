from django.db import models

# Create your models here.


class Adotante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    data_nascimento = models.DateField()

    def __str__(self) -> str:
        return self.nome
