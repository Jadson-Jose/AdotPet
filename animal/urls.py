from django.urls import path
from . import views

urlpatterns = [
    path('animais/', views.lista_animais, name='lista_animais'),
    path('animais/<int:pk>/', views.detalhe_animal, name='detalhe_animal'),
    path('animais/novo/', views.criar_animal, name='criar_animal'),
    path('animais/<int:pk>/editar/', views.editar_animal, name='editar_animal'),
    path('animais/<int:pk>/deletar/', views.deletar_animal, name='deletar_animal'),

    # Adicione rotas semelhantes para Adotante, Adoção e Abrigo
]
