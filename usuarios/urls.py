from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastrar, name='cadastro_usuario'),
    path('logar/', views.logar, name='login_usuario'),
    path('logout/', views.sair, name='logout_usuario')

]