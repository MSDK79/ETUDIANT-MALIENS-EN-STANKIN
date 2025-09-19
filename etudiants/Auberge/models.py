from django.db import models
from django.db.models import Count
from datetime import date
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Etudiant(models.Model):
    numEtudiant=models.CharField(max_length=10, null=True)
    nom=models.CharField(max_length=80,null=False)
    prenom=models.CharField(max_length=80,null=False)
    numPossport=models.CharField(max_length=20, null=True)
    telephone=models.CharField(max_length=20, null=True)
    email=models.CharField(max_length=80, null=False, default="di@gmail.com")
    domFormation=models.CharField(max_length=90, null=False,default="informatique")
    dateNaissance=models.DateField()
    typeBourse=(('boursierEtatMalien','boursier Etat Malien'),('boursierEtatRusse','boursier Etat Russe'),('Contractuel','Contractuel'),   )
    type=models.CharField(choices=typeBourse, default="Boursier Etat Malien")
    GENRE=(('m','M'),('f','F'))
    sexe=models.CharField(choices=GENRE)
    class Meta:
        verbose_name= ("Etudiant")
        verbose_name_plural= ("Etudiant")
    def __str__(self):
        return  f" {self.numEtudiant}  {self.nom} {self.prenom} "
    
    
class Auberge(models.Model):
    nomAuberge=models.CharField(max_length=100)
    adresseAuberge=models.CharField(max_length=200, null=False)
    description=models.TextField(max_length=500,null=True)
    class Meta:
        verbose_name= ("Auberge")
        verbose_name_plural= ("Auberge")
    def __str__(self):
        return self.nomAuberge
class Etage (models.Model):

    nomEtage=models.CharField(max_length=50, null=False)
    numAuberge=models.ForeignKey(Auberge,on_delete=models.CASCADE)
    class Meta:
        verbose_name= ("Etage")
        verbose_name_plural= ("Etage")
    filter=('nomEtage',)
    def __str__(self):
        return self.nomEtage
class TypeChambre (models.Model):
    numTypeChambre= models.CharField(max_length=10, primary_key=True)
    TYPECH=(('Chambre pour quatre personnes', 'Chambre_4'), ('chambre pour deux personnes', 'Chambre_2') )
    TYPE=models.CharField(choices=TYPECH)
   
    class Meta:
        verbose_name= ("Type de Chambre")
        verbose_name_plural= ("Types de Chambre")
    def __str__(self):
        return f" {self.numTypeChambre} {self.TYPE} "
class Chambre(models.Model):
    numTypeChambre=models.ForeignKey(TypeChambre, on_delete=models.CASCADE)

    nomChambre=models.CharField(max_length=50, default='Chambre')
    etage=models.ForeignKey(Etage, on_delete=models.CASCADE, default='01')
    class Meta:
        verbose_name= ("Chambre")
        verbose_name_plural= ('Chambres')
    def __str__(self):
        return self.nomChambre
class Habiter(models.Model):
    numHabiter=models.CharField(max_length=10, primary_key=True)
    numEtudiant=models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    numChambre=models.ForeignKey(Chambre,  on_delete=models.CASCADE,related_name="vivre")
    nombre= models.IntegerField(max_length=4, default=1)

    class Meta:
        verbose_name= ("Habiter")
        verbose_name_plural= ('Habiter')
    
class CustomUser(AbstractUser):
    
   pass 