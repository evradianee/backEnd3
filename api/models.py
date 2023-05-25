from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid 
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class Utilisateur(models.Model):
    prenom = models.CharField(max_length=200 , null=False, blank=False)
    pseudo = models.CharField(max_length=200 , null=False, blank=False)
    email = models.CharField(max_length=200 , null=False, blank=False)
    password = models.CharField(max_length=200 , null=False, blank=False)
    payment= models.BooleanField(default=False) 
    nbr_sc=models.IntegerField(default=0)
    
    
    def __str__(self) :
        return self.prenom

class Admin(models.Model):
    pseudo_admin = models.CharField(max_length=200 , null=False, blank=False)
    password_admin = models.CharField(max_length=200 , null=False, blank=False)

    def __str__(self) :
        return self.pseudo_admin



class Employe(models.Model):
    prenom_employe = models.CharField(max_length=200 , null=False, blank=False)
    pseudo_employe = models.CharField(max_length=200 , null=False, blank=False)
    password_employe = models.CharField(max_length=200 , null=False, blank=False)      
    specialite_employe = models.CharField(max_length=200 , null=False, blank=False)
    description_employe = models.CharField(max_length=200 , null=False, blank=False)
    image_employe = models.ImageField(upload_to='Images/', null=True)
    support_divinatoire_employe = models.CharField(max_length=200 , null=False, blank=False)
    statut_employe = models.BooleanField(default=True)   
    nbr_utilisateurs = models.IntegerField(default= 0)

    def __str__(self) :
        return self.prenom_employe


class conversationinfo(models.Model):
    conversationId = models.CharField( max_length=200)
    pseudo_employe = models.CharField(max_length=200 ,default=None) 
    pseudo = models.CharField(max_length=200 , null=False, blank=False,default=None)

class Message(models.Model):
    conversationi = models.CharField(max_length=200 , null=False, blank=False,default=None)
    sender = models.CharField(max_length=200 , null=False, blank=False,default=None)
    text = models.TextField()

class timing(models.Model):
    nbr_minutes = models.CharField( max_length=200)
    price = models.FloatField(max_length=100)

class historiqueinfo(models.Model):
    historiqueId = models.CharField( max_length=200)
    pseudo_employe = models.CharField(max_length=200 ,default=None) 
    pseudo = models.CharField(max_length=200 , null=False, blank=False,default=None)


class Message_historique(models.Model):
    historiquei = models.CharField(max_length=200 , null=False, blank=False,default=None)
    sender = models.CharField(max_length=200 , null=False, blank=False,default=None)
    text = models.TextField()    




   

    



