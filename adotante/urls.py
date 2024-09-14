from django.urls import path
from . import views

urlpatterns = [
    path('adotantes/', views.lista_adotantes, name='lista_adotantes'),
    path('adotantes/<int:pk>/', views.detalhe_adotante, name='detalhe_adotante'),
    path('adotantes/novo/', views.criar_adotante, name='criar_adotante'),
    path('adotantes/<int:pk>/editar/',
         views.editar_adotante, name='editar_adotante'),
    path('adotantes/<int:pk>/deletar/',
         views.deletar_adotante, name='deletar_adotante'),
]
