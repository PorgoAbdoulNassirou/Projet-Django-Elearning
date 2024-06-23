from django.shortcuts import render
def afficherAboutUs(request):
    return render(request, 'about.html')
# Create your views here.

def afficherContacte(request):
    return render(request, 'contact.html')


def afficherCours(request):
    return render(request, 'courses.html')


def afficherhome(request):
    return render(request, 'home.html')


def afficherlogin(request):
    return render(request, 'login.html')

def afficherplaylist(request):
    return render(request, 'playlist.html')


def afficherprofile(request):
    return render(request, 'profile.html')

def afficherregister(request):
    return render(request, 'register.html')


def afficherlogin_number(request):
    return render(request, 'login_number.html')


def afficherteacherprofile(request):
    return render(request, 'teacher_profile.html')


def afficherteacher(request):
    return render(request, 'teachers.html')


def afficherupdate(request):
    return render(request, 'update.html')


def affichervideos(request):
    return render(request, 'watch-video.html')



from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Utilisateur, Cours
from .forms import InscriptionForm, ConnexionForm  # Importer les formulaires

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, 'Inscription réussie. Veuillez vérifier votre email pour valider votre inscription.')
            return redirect('login')
    else:
        form = InscriptionForm()
    return render(request, 'register.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('courses')
            else:
                messages.error(request, 'Identifiant ou mot de passe incorrect.')
    else:
        form = ConnexionForm()
    return render(request, 'login.html', {'form': form})

@login_required
def deconnexion(request):
    logout(request)
    return redirect('login')

@login_required
def gestion_cours(request):
    cours = Cours.objects.filter(niveau=request.user.niveau)
    return render(request, 'courses.html', {'cours': cours})

