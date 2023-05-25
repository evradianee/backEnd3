from rest_framework import serializers
from .models import Utilisateur , Employe , Admin  , conversationinfo , Message , timing , historiqueinfo , Message_historique


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'

class EmployeSerializer(serializers.ModelSerializer):
    image_employe = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = Employe
        fields = ('prenom_employe', 'pseudo_employe', 'password_employe', 'specialite_employe', 'description_employe', 'image_employe',  'support_divinatoire_employe','statut_employe','nbr_utilisateurs')


class conversationinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = conversationinfo
        fields = ('conversationId','pseudo_employe','pseudo')  



class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('conversationi','sender','text')


class timingSerializer(serializers.ModelSerializer):
    class Meta:
        model = timing
        fields = '__all__'

class historiqueinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = historiqueinfo
        fields = '__all__'        
         
class Message_historiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message_historique
        fields = '__all__'

