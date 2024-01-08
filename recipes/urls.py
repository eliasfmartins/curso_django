from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe ),
]
# usa se <nome param> para pegar o valor dinamico
#dentro do < passar o tipo de propriedade vai ser aceito como parametro no meu caso <int:>
# tem varios tipos na documentação
