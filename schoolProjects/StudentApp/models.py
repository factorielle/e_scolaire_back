from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser



# modele de base utilisateur
class User(AbstractUser):
    ROLE_CHOICES = [
        ('parent', 'Parent'),
        ('prof', 'Professeur'),
        ('eleve', 'Élève'),
        ('admin', 'Administrateur'),
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=255)
    password = models.CharField(max_length=255)  
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)  # Hasher le mot de passe avant de l'enregistrer
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
  

# Modèle pour la table Matiere
class Matiere(models.Model):
    libelle = models.CharField(max_length=100)
    coefficient = models.PositiveIntegerField()

# Modèle pour la table Note
class Note(models.Model):
    valeur = models.DecimalField(max_digits=5, decimal_places=2)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)

# Modèle pour la table Classe
class Classe(models.Model):
    nom = models.CharField(max_length=100)
    effectif = models.PositiveIntegerField()

# Table d'association pour la relation plusieurs à plusieurs entre Classe et Eleve
class Admission(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    eleve = models.ForeignKey('Eleve', on_delete=models.CASCADE)
    annee = models.IntegerField()

# Modèle pour la table Eleve
class Eleve(User):
    classes = models.ManyToManyField(Classe, through='Admission')
    date_naissance = models.DateField()


# Modele pour la table parent
class Parent(User):
    pass

# Modèle pour la table Inscription
class Inscription(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    date_inscription = models.DateField()
    

# Modèle pour la table Professeur
class Professeur(User):
    matieres = models.ManyToManyField(Matiere, through='Enseignement')

# Table d'association pour la relation plusieurs à plusieurs entre Professeur et Matiere
class Enseignement(models.Model):
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)

# Modèle pour la table Admin
class Admin(User):
   pass

# Modèle pour la table Dossier
class Dossier(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    update_at = models.DateTimeField(auto_now=True)
    update_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dossiers_updated')

# Modèle pour la table Rapport
class Rapport(models.Model):
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    update_at = models.DateTimeField(auto_now=True)
    update_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rapports_updated')

# Modèle pour la table Appreciation
class Appreciation(models.Model):
    rapport = models.ForeignKey(Rapport, on_delete=models.CASCADE)
    texte = models.TextField()

# Modèle pour la table Bulletin
class Bulletin(models.Model):
    rapport = models.ForeignKey(Rapport , null=True,  on_delete=models.CASCADE)
    # Ajoutez les champs nécessaires pour le bulletin

# Modèle pour la table Certificat
class Certificat(models.Model):
    rapport = models.ForeignKey(Rapport, null=True, on_delete=models.CASCADE)
    texte = models.TextField()
