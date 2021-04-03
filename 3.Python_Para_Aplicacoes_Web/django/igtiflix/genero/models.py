from django.db import models

class Genero(models.Model):
    descricao = models.CharField(max_length = 50)

    def __str__(self):
        return self.descricao

    objects = models.Manager()
