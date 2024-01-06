from django.urls import path
from recipes.views import home ,sobre, _contato

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', _contato),
]
