from django.urls import path
from . import views

urlpatterns = [
    path('abrigo/', views.lista_abrigos, name='lista_abrigos'),
    path('abrigo/<int:pk>/', views.detalhe_abrigo, name='detalhe_abrigo'),
    path('abrigo/novo/', views.criar_abrigo, name='criar_abrigo'),
    path('abrigo/<int:pk>/editar/', views.editar_abrigo, name='editar_abrigo'),
    path('abrigo/<int:pk>/deletar_abrigo/',
         views.deletar_abrigo, name='deletar_abrigo'),
]
