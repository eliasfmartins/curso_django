from django.shortcuts import render
from utils.recipes.factory import make_recipe

# HTTP REQUEST
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes':[make_recipe() for _ in range(10)]
    } )
    
# return HTTP Response
# Create your views here.
def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
    } )

