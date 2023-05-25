from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import StripeCheckoutView


urlpatterns = [
       
    path('Utilisateur_create/', views.CreateUtilisateur, name='Utilisateur_create'),
    path('Utilisateur_authentification/',views.Authentification, name='Utilisateur_create'),
    path('Admin_authentification/',views.Authentification_Admin, name='Admin_authentification'),
    path('Employe_create/',views.CreateEmploye, name='Employe_create'),
    path('Authentification_Employe/',views.Authentification_Employe, name='Authentification_Employe'),
    path('Createconversation/',views.Createconversation, name='Createconversation'),
    path('CreateMessage/',views.CreateMessage, name='CreateMessage'),
    path('StripeCheckoutView/<pk>/',StripeCheckoutView.as_view(), name='StripeCheckout'),
    path('change/',views.change, name='change'),
    path('change_employe/',views.change_employe, name='change_employe'),
    path('update_nbr_min/',views.update_nbr_min, name='update_nbr_min'),
    path('conversation_utilisateur/',views.conversation_utilisateur, name='conversation_utilisateur'),
    path('Createhistorique/',views.Createhistorique, name='Createhistorique'),
    path('historique_utilisateur/',views.historique_utilisateur, name='historique_utilisateur'),
    path('CreateMessage_historique/',views.CreateMessage_historique, name='CreateMessage_historique'),
    path('pseudo_utilisateur_bd/',views.pseudo_utilisateur_bd, name='pseudo_utilisateur_bd'),
    path('pseudo_employe_bd/',views.pseudo_employe_bd, name='pseudo_employe_bd'),
    path('number_utilisateur/',views.number_utilisateur, name='number_utilisateur'),
    
   
   
  
]  