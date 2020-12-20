from django.db import models


class Mission(models.Model):
    NomMission = models.CharField(max_length=50, unique=True)
    DateDebut = models.DateField()
    DateFin = models.DateField()
    Description = models.CharField(max_length=2000)
    Nigend = models.ForeignKey('Personnel', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.NomMission


class Personnel(models.Model):
    Nigend = models.CharField(max_length=6, unique=True)
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=30)
    Grade = models.CharField(max_length=52)
    Tel = models.CharField(max_length=30)
    Mail = models.EmailField(max_length=100)

    def __str__(self):
        return self.Nom


class Materiel(models.Model):
    Materiel = models.CharField(max_length=20, unique=True)
    ChampControle = models.CharField(max_length=30)

    def __str__self(self):
        return self.Materiel
