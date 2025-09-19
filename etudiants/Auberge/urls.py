from django.urls import path
from . import views



urlpatterns = [
    path('home', views.page_accueil, name="home"),
    path('ajouter',views.ajout, name="ajouter_un_etudiant"),
    path('affiche', views.affiche, name="affiche"),
    path('modifier/ <int:pk>/', views.modifier_e, name='modifier_Etudiant'),
    path('delete/<int:pk>/', views.delete_e, name='supriudiant'),
    path('ajout_aub/', views.enregitrer_auberge),
    path('etage/', views.ajout_etage),
    path('auberge', views.liste_aub, name='list_aub'),
    path('list_etage', views.liste_etage, name='list_etage'),
    path('typechambre', views.ajout_type_chambre, name='type_chambre'),
    path('ajoutchambre', views.ajout_chambre, name='ajout_chambre'),
    path('etage_par_auberge/<int:pk>/', views.les_etages_de_aub, name='les_etages_aub'),
    path('liste_type_chambre', views.liste_type_chambre, name='list_type_chambre'),
    path('liste_chambre/<int:pk>/', views.liste_chambre, name='liste_chamb'),
    path('ajouthabiter', views.ajout_habiter, name='ajout_habite'),
    path('listeetudiant', views.liste_etudiant, name='liste_etudiant'),
    path('listehabiter/<int:pk>/', views.liste_habiter, name='liste_habiter'),
    path('contact', views.contact, name='contact'),
    path('inscription', views.inscription, name='inscription'),
    path('', views.login, name='login'),
   
   



]   
