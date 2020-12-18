from django.db import models


class Mission(models.Model):
    NomMission = models.CharField(max_length=50, unique=True)
    DateDebut = models.DateField()
    DateFin = models.DateField()
    Description = models.CharField(max_length=2000)
    Personnels = models.ForeignKey('Nigend', on_delete=models.CASCADE,)

    def __str__self(self):
        return self.NomMission


class Personnel(models.Model):
    Nigend = models.CharField(max_length=6, unique=True)
    Nom = models.CharField(max=50)
    Prenom = models.CharField(max_length=30)
    Tel = models.CharField(max_length=30)
    Mail = models.CharField(max_length=100)

    def __str__self(self):
        return self.Nom


class Materiel(models.Model):
    Materiel = models.CharField(max_length=20, unique=True)
    ChampControle = models.CharField(max_length=30)

    def __str__self(self):
        return self.Materiel
