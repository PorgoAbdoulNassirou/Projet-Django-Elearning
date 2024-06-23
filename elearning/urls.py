from django.urls import path
from . import views
from .views import afficherAboutUs, afficherprofile, afficherregister, afficherteacherprofile, afficherteacher, \
    affichervideos, afficherupdate, afficherContacte, afficherCours, afficherhome, afficherlogin, afficherplaylist, \
    afficherlogin_number

urlpatterns = [
    path('', afficherAboutUs, name='about'),
    path('contacte', afficherContacte, name='contact'),
    path('loginnumber', afficherlogin_number, name='login_number'),
    path('cours', afficherCours, name='courses'),
    path('home', afficherhome, name='home'),
    path('login', afficherlogin, name='login'),
    path('playlist', afficherplaylist, name='playlist'),
    path('profile', afficherprofile, name='profile'),
    path('signup', afficherregister, name='register'),
    path('teacherprofile', afficherteacherprofile, name='teacher_profile'),
    path('teacher', afficherteacher, name='teachers'),
    path('update', afficherupdate, name='update'),
    path('videos', affichervideos, name='videos'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='login'),
    path('deconnexion/', views.deconnexion, name='register'),
    path('gestion-cours/', views.gestion_cours, name='courses'),
]

