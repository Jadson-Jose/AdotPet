from django.urls import path
from . import views

urlpatterns = [
    path('adocoes/', views.lista_adocoes, name='lista_adocoes'),
    path('adocoes/<int:pk>/', views.detalhe_adocao, name='detalhe_adocao'),
    path('adocoes/novo/', views.criar_adocao, name='criar_adocao'),
    path('adocoes/<int:pk>/editar/', views.editar_adocao, name='editar_adocao'),
    path('adocoes/<int:pk>/deletar/', views.deletar_adocao, name='deletar_adocao'),
]
