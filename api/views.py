from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UtilisateurSerializer, EmployeSerializer  , conversationinfoSerializer , MessageSerializer , historiqueinfoSerializer , Message_historiqueSerializer
from api.models import Utilisateur , Admin , Employe , conversationinfo , Message , timing , historiqueinfo , Message_historique
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
import json 
from django.http import JsonResponse
from django.core.serializers import serialize
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
import uuid
from django.conf import settings
import stripe
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import redirect
stripe.api_key = settings.STRIPE_SECRET_KEY





# Create your views here.



@api_view(['POST'])
def CreateUtilisateur(request):
    serializer = UtilisateurSerializer(data=request.data)  
    if serializer.is_valid():
        serializer.save()
    return  Response(serializer.data)  

@api_view(['POST'])
def Authentification(request):
    user=request.data['pseudo']
    mdp=request.data['password']
    try :
        connex = Utilisateur.objects.get(pseudo=user , password=mdp)
    except ObjectDoesNotExist:
        connex = None

    if  connex is None :
            return Response(False)
    else :
        if connex.password == mdp and connex.pseudo :
            return Response(True) 


@api_view(['POST'])      
def Authentification_Admin(request) :
    adminn=request.data['pseudo_admin']
    mdp=request.data['password_admin']
    try :
        connex = Admin.objects.get(pseudo_admin=adminn , password_admin=mdp)
    except ObjectDoesNotExist:
        connex = None

    if  connex is None :
            return Response(False)
    else:
        
        if connex.password_admin == mdp and connex.pseudo_admin == adminn:
            return Response(True)
    



@api_view(['POST'])
def CreateEmploye(request):
    nm =request.data['prenom_employe']
    pnm=request.data['pseudo_employe']
    mdp=request.data['password_employe']
    sps=request.data['specialite_employe']
    dsm=request.data['description_employe']
    img=request.data['image_employe']
    sde=request.data['support_divinatoire_employe']
    Employe.objects.create(prenom_employe=nm, pseudo_employe=pnm, password_employe=mdp, specialite_employe=sps , description_employe=dsm, image_employe=img, support_divinatoire_employe=sde )
    return Response(True)


class ReturnEmploye(viewsets.ModelViewSet):
    serializer_class = EmployeSerializer

    def get_queryset(self):
         employe_spec = Employe.objects.all()
         return employe_spec
    def retrieve(self, request, *args, **kwargs):
        params=kwargs
        employes = Employe.objects.filter(pseudo_employe=params['pk'])
        serializer = EmployeSerializer(employes, many=True)
        return Response(serializer.data)



class ReturnUtilisateur(viewsets.ModelViewSet):
    serializer_class = UtilisateurSerializer

    def get_queryset(self):
         utilisateur_spec = Utilisateur.objects.all()
         return utilisateur_spec

    def retrieve(self, request, *args, **kwargs):
        params=kwargs
        utilisateurs = Utilisateur.objects.filter(pseudo=params['pk'])
        serializer = UtilisateurSerializer(utilisateurs, many=True)
        return Response(serializer.data) 
        
@api_view(['POST'])
def change(request):
    name=request.data["pseudo"]
    nbr_sc_front = int(request.data["nbr_sc"])*60
    user = Utilisateur.objects.get(pseudo=name)
    sc=user.nbr_sc
    sc_t=sc+nbr_sc_front
    Utilisateur.objects.filter(pseudo=name).update(payment=True, nbr_sc = sc_t)
    return Response('done')


@api_view(['POST'])
def change_employe(request):
    name=request.data["pseudo_employe"]
    stat=request.data["statut_employe"]
    Employe.objects.filter(pseudo_employe=name).update(statut_employe=stat)
    return Response('done')    
        


@api_view(['POST'])      
def Authentification_Employe(request) :
    employee=request.data['pseudo_employe']
    mdp=request.data['password_employe']
    try :
        connex = Employe.objects.get(pseudo_employe=employee , password_employe=mdp)
    except ObjectDoesNotExist:
        connex = None

    if  connex is None :
            return Response(False)
    else:
        if connex.password_employe == mdp and connex.pseudo_employe == employee:
            return Response(True)   

@api_view(['POST'])  
def Createconversation(request):
    employeee=request.data['pseudo_employe']
    user=request.data['pseudo']
    convid = uuid.uuid4()
    conversationinfo.objects.create(conversationId=convid , pseudo_employe=employeee , pseudo=user)
    return Response(convid)


class Returnconversationinfo(viewsets.ModelViewSet):
    serializer_class = conversationinfoSerializer

    def get_queryset(self):
         conversation_spec = conversationinfo.objects.all()
         return conversation_spec

    def retrieve(self, request, *args, **kwargs):
        params=kwargs
        conversations = conversationinfo.objects.filter(pseudo=params['pk'])
        serializer = conversationinfoSerializer(conversations, many=True)
        
        return Response(serializer.data)     

class Returnconversation_employe(viewsets.ModelViewSet):
    serializer_class = conversationinfoSerializer

    def get_queryset(self):
         conversation_spec = conversationinfo.objects.all()
         return conversation_spec

    def retrieve(self, request, *args, **kwargs):
        params=kwargs
        conversationss = conversationinfo.objects.filter(pseudo_employe=params['pk'])
        serializer = conversationinfoSerializer(conversationss, many=True)
        return Response(serializer.data)    

@api_view(['POST'])  
def CreateMessage(request):
    conv=request.data['conversationi']
    send=request.data['sender']
    txt = request.data['text']
    Message.objects.create(conversationi=conv , sender=send , text=txt)
    data={
        "conversationi":conv,
        "sender":send,
        "text":txt
    }


    return Response(data)  
    
            

class ReturnMessage(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
         Message_spec = Message.objects.all()
         return Message_spec

    def retrieve(self, request, *args, **kwargs):
        params=kwargs
        messages = Message.objects.filter(conversationi=params['pk'])
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)    


class StripeCheckoutView(APIView):
    def post(self, request,*args,**kwargs) : 

     nb_minutes=self.kwargs['pk']
     try:

         nbb_minutes=timing.objects.get(nbr_minutes=nb_minutes)
         checkout_session = stripe.checkout.Session.create(
             line_items=[
                 {
                    
                     'price_data':{
                        'currency':'eur',
                        'unit_amount': round((nbb_minutes.price)*100),
                        'product_data':{
                            'name': nbb_minutes.nbr_minutes + 'min',
                        } 
                     },
                     'quantity': 1,
                 },
             ],
             payment_method_types = ['card',],
             mode='payment',
             success_url= settings.SITE_URL+ '?success=true&session_id={CHEKOUT_SESSION_ID}',
             cancel_url=settings.SITE_URL + '?canceled=true',
         )
         return redirect(checkout_session.url)
     except :
         return Response('erreur : something went wrong')


@api_view(['POST'])
def update_nbr_min(request):
    user= request.data['pseudo']
    empl=request.data['pseudo_employe']
    nbr_sc_front = request.data['nbr_sc']
    empll = Employe.objects.get(pseudo_employe=empl)
    number = empll.nbr_utilisateurs - 1

    utili=Utilisateur.objects.get(pseudo=user)
    sc=utili.nbr_sc
    scc=sc-int(nbr_sc_front)
    if scc >= 0 :
        Utilisateur.objects.filter(pseudo=user).update(nbr_sc = scc)
        return Response(True)
    else :
        Utilisateur.objects.filter(pseudo=user).update(nbr_sc = 0, payment=False)   
        Message.objects.filter(sender=user).delete()
        conversationinfo.objects.filter(pseudo=user).delete()
        Employe.objects.filter(pseudo_employe=empl).update(nbr_utilisateurs=number)
        return Response(False) 


@api_view(['POST'])
def conversation_utilisateur(request):
    emp=request.data['pseudo_employe']
    user= request.data['pseudo']
    
    try:   
        conv = conversationinfo.objects.get(pseudo_employe=emp,pseudo=user)
    except ObjectDoesNotExist:  
        conv = None
    if conv is None :
        return Response(True)
    else:
        if conv.pseudo_employe == emp and conv.pseudo == user:
            return Response(False)


@api_view(['POST'])  
def Createhistorique(request):
    employeee=request.data['pseudo_employe']
    user=request.data['pseudo']
    hisvid = uuid.uuid4()
    historiqueinfo.objects.create(historiqueId=hisvid , pseudo_employe=employeee , pseudo=user)
    return Response(hisvid)       

@api_view(['POST'])
def historique_utilisateur(request):
    emp=request.data['pseudo_employe']
    user= request.data['pseudo']
    try:   
        hist = historiqueinfo.objects.get(pseudo_employe=emp,pseudo=user)
    except ObjectDoesNotExist:  
        hist = None
    if hist is None :
        return Response(True)
    else:
        if hist.pseudo_employe == emp and hist.pseudo == user:
            return Response(False)       


class Returnhistoriqueinfo(viewsets.ModelViewSet):
    serializer_class = historiqueinfoSerializer

    def get_queryset(self):
         historique_spec = historiqueinfo.objects.all()
         return historique_spec

    def retrieve(self, request, *args, **kwargs):
        params=kwargs
        historiques = historiqueinfo.objects.filter(pseudo=params['pk'])
        serializer = historiqueinfoSerializer(historiques, many=True)
        
        return Response(serializer.data)   



@api_view(['POST'])  
def CreateMessage_historique(request):
    hist=request.data['historiquei']
    send=request.data['sender']
    txt = request.data['text']
    Message_historique.objects.create(historiquei=hist , sender=send , text=txt)
    data={
        "historiquei":hist,
        "sender":send,
        "text":txt
    }


    return Response(data)              

class ReturnMessage_historique(viewsets.ModelViewSet):
    serializer_class = Message_historiqueSerializer

    def get_queryset(self):
         Message_historique_spec = Message_historique.objects.all()
         return Message_historique_spec

    def retrieve(self, request, *args, **kwargs):
        params=kwargs
        messages_historique = Message_historique.objects.filter(historiquei=params['pk'])
        serializer = Message_historiqueSerializer(messages_historique, many=True)
        return Response(serializer.data)         


class Returnhistoriqueinfo_employe(viewsets.ModelViewSet):
    serializer_class = historiqueinfoSerializer

    def get_queryset(self):
         historique_spec = historiqueinfo.objects.all()
         return historique_spec

    def retrieve(self, request, *args, **kwargs):
        params=kwargs
        historiques = historiqueinfo.objects.filter(pseudo_employe=params['pk'])
        serializer = historiqueinfoSerializer(historiques, many=True)
        
        return Response(serializer.data)        



@api_view(['POST'])
def pseudo_utilisateur_bd(request):
    user= request.data['pseudo']
    try:   
        userr = Utilisateur.objects.get(pseudo=user)
    except ObjectDoesNotExist:  
        userr = None
            
    try :
        userrr=Employe.objects.get(pseudo_employe=user)
    except    ObjectDoesNotExist:
        userrr = None


    if userr is None and userrr is None :
        return Response(True)
    if userr is not None and userrr is None :
        return Response(False)  

    if userrr is not None and userr is None :
        return Response(False)

    else:
        if userr.pseudo == user and userrr.pseudo_employe == user :
            return Response(False)             

@api_view(['POST'])
def pseudo_employe_bd(request):
    user= request.data['pseudo_employe']
    try:   
        userr = Utilisateur.objects.get(pseudo=user)
    except ObjectDoesNotExist:  
        userr = None
            
    try :
        userrr=Employe.objects.get(pseudo_employe=user)
    except    ObjectDoesNotExist:
        userrr = None


    if userr is None and userrr is None :
        return Response(True)
    if userr is not None and userrr is None :
        return Response(False)  

    if userrr is not None and userr is None :
        return Response(False)

    else:
        if userr.pseudo == user and userrr.pseudo_employe == user :
            return Response(False)   


@api_view(['POST'])
def number_utilisateur(request):
    emp=request.data['pseudo_employe']
    empl=Employe.objects.get(pseudo_employe=emp)
    number = int(empl.nbr_utilisateurs) + 1
    Employe.objects.filter(pseudo_employe=emp).update(nbr_utilisateurs=number)
    return Response(True)      



       
        


             

     




    




     




