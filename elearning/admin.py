from django.contrib import admin
from .models import Utilisateur, Matiere, Chapitre, Lecon, Cours, Exercice, Evaluation, Inscription, Abonnement, Transaction

admin.site.register(Utilisateur)
admin.site.register(Matiere)
admin.site.register(Chapitre)
admin.site.register(Lecon)
admin.site.register(Cours)
admin.site.register(Exercice)
admin.site.register(Evaluation)
admin.site.register(Inscription)
admin.site.register(Abonnement)
admin.site.register(Transaction)

# Register your models here.
