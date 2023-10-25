from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('recibe-formulario-para-enviar-email/', views.procesar_envio_email,
         name='procesar_envio_email'),
]
