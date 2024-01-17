from django.urls import path
from . import  views

#recipes:recipe
app_name ='recipes'

urlpatterns = [
    path('', views.home, name='home') ,
    path('recipes/category/<int:category_id>/', views.category, name='category' ),
    path('recipes/<int:id>/', views.recipe, name='recipe' ),
]
# usa se <nome param> para pegar o valor dinamico
#dentro do < passar o tipo de propriedade vai ser aceito como parametro no meu caso <int:>
# tem varios tipos na documentação
#
