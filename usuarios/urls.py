from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastrar, name='cadastro_usuario'),
    path('login/', views.logar, name='login_usuario')

]