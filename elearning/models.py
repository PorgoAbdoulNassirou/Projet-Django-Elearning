from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Utilisateur(AbstractUser):
    ROLES = [
        ('eleve', 'Élève'),
        ('enseignant', 'Enseignant'),
        ('administrateur', 'Administrateur'),
    ]
    niveau = models.CharField(max_length=10, choices=[
        ('6e', '6e'),
        ('5e', '5e'),
        ('4e', '4e'),
        ('3e', '3e'),
        ('2e', '2e'),
        ('1e', '1e'),
        ('terminale', 'Terminale'),
    ])
    role = models.CharField(max_length=15, choices=ROLES)
    abonnement = models.ForeignKey('Abonnement', on_delete=models.SET_NULL, null=True, blank=True)
    code_authentification = models.CharField(max_length=6)
    valide = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name='utilisateur_set')
    user_permissions = models.ManyToManyField(Permission, related_name='utilisateur_permissions_set')


class Matiere(models.Model):
    nom = models.CharField(max_length=100)

class Chapitre(models.Model):
    titre = models.CharField(max_length=100)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)

class Lecon(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE)
    enseignant = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, limit_choices_to={'role': 'enseignant'})

class Cours(models.Model):
    TYPES = [
        ('texte', 'Texte'),
        ('video', 'Vidéo'),
        ('image', 'Image'),
        ('pdf', 'PDF'),
    ]
    titre = models.CharField(max_length=100)
    description = models.TextField()
    niveau = models.CharField(max_length=10)
    type = models.CharField(max_length=10, choices=TYPES)
    contenu = models.TextField()
    enseignant = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, limit_choices_to={'role': 'enseignant'})

class Exercice(models.Model):
    TYPES = [
        ('qcm', 'QCM'),
        ('question-reponse', 'Question-Réponse'),
        ('calcul', 'Calcul'),
    ]
    type = models.CharField(max_length=20, choices=TYPES)
    question = models.TextField()
    reponse = models.TextField()
    lecon = models.ForeignKey(Lecon, on_delete=models.CASCADE)

class Evaluation(models.Model):
    type = models.CharField(max_length=20, choices=Exercice.TYPES)
    question = models.TextField()
    reponse_attendue = models.TextField()
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    enseignant = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, limit_choices_to={'role': 'enseignant'})

class Inscription(models.Model):
    eleve = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, limit_choices_to={'role': 'eleve'})
    date_inscription = models.DateTimeField(auto_now_add=True)
    niveau = models.CharField(max_length=10)
    code_authentification = models.CharField(max_length=6)
    valide = models.BooleanField(default=False)

class Abonnement(models.Model):
    TYPES = [
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    ]
    type = models.CharField(max_length=10, choices=TYPES)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

class Transaction(models.Model):
    MOYENS_PAIEMENT = [
        ('orange_money', 'Orange Money'),
        ('moov_money', 'Moov Money'),
    ]
    eleve = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, limit_choices_to={'role': 'eleve'})
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    moyen_paiement = models.CharField(max_length=20, choices=MOYENS_PAIEMENT)
    date_transaction = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20)

# Create your models here.
