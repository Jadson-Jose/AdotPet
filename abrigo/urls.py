from django.urls import path
from . import views

urlpatterns = [
    path('abrigos/', views.lista_abrigo, name='lista_abrigo'),
    path('abrigos/<int:pk>/', views.detalhe_abrigo, name='detalhe_abrigo'),
    path('abrigos/novo/', views.criar_abrigo, name='criar_abrigo'),
    path('abrigos/<int:pk>/editar/', views.editar_abrigo, name='editar_abrigo'),
    path('abrigos/<int:pk>/deletar_abrigo/',
         views.deletar_abrigo, name='deletar_abrigo'),
]
