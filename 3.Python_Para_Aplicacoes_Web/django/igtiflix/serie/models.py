from django.db import models

class Serie(models.Model):
    nome = models.CharField(max_length = 100)
    id_genero = models.ForeignKey('genero.Genero', on_delete = models.PROTECT)

    def __str__(self):
        return self.nome

    objects = models.Manager()