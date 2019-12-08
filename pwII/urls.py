from django.urls import path,include
from . import views

urlpatterns = [   
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('dash', views.dash, name='dash'),
    path('marcar/<int:pk>/', views.marcar, name='marcar'),
    path('historico/<int:pk>/', views.historico, name='historico'),
    path('minha_conta', views.minha_conta, name='minha_conta'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('cadUser', views.cadUser, name='cadUser'),
    path('salvar_consulta', views.salvar_consulta, name='salvar_consulta'),
    path('cadEnd', views.cadEnd, name='cadEnd'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('list_consulta/<int:pk>/', views.list_consulta, name='list_consulta'),
    path('confimar_consulta', views.confimar_consulta, name='confimar_consulta'),
    path('cancelar_consulta/<int:pk>/', views.cancelar_consulta, name='cancelar_consulta'),
    path('alterar_consulta/<int:pk>/', views.alterar_consulta, name='alterar_consulta'),
    path('confirmar_alteracoes', views.confirmar_alteracoes, name='confirmar_alteracoes'),
    path('alterar_meus_dados/<int:pk>/', views.alterar_meus_dados, name='alterar_meus_dados'),
    path('salvar_meus_dados', views.salvar_meus_dados, name='salvar_meus_dados'),
    path('excluir_historico/<int:pk>/', views.excluir_historico, name='excluir_historico'),
    
    
]
