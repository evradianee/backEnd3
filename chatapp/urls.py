"""chatapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import ReturnEmploye,ReturnUtilisateur,Returnconversationinfo,Returnconversation_employe,ReturnMessage , Returnhistoriqueinfo , ReturnMessage_historique , Returnhistoriqueinfo_employe
from django.conf import settings
from django.conf.urls.static import static



router = routers.DefaultRouter()
router.register(r'ReturnEmploye',ReturnEmploye,basename='ReturnEmploye')
router.register(r'ReturnUtilisateur',ReturnUtilisateur,basename='ReturnUtilisateur')
router.register(r'Returnconversationinfo',Returnconversationinfo,basename='Returnconversationinfo')
router.register(r'Returnconversation_employe',Returnconversation_employe,basename='Returnconversation_employe')
router.register(r'ReturnMessage',ReturnMessage,basename='ReturnMessage')
router.register(r'Returnhistoriqueinfo',Returnhistoriqueinfo,basename='Returnhistoriqueinfo')
router.register(r'ReturnMessage_historique',ReturnMessage_historique,basename='ReturnMessage_historique')
router.register(r'Returnhistoriqueinfo_employe',Returnhistoriqueinfo_employe,basename='Returnhistoriqueinfo_employe')





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/', include(router.urls)),
    
  

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

