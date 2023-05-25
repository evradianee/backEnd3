from django.contrib import admin
from . models import Utilisateur , Admin , Employe , conversationinfo , Message , timing, historiqueinfo, Message_historique
# Register your models here.


admin.site.register(Utilisateur)
admin.site.register(Admin)
admin.site.register(Employe)
admin.site.register(historiqueinfo)
admin.site.register(conversationinfo)
admin.site.register(Message)
admin.site.register(timing)
admin.site.register(Message_historique)
