from django.shortcuts import render


# HTTP REQUEST
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name':'Elias the Fodao'
    } )
    # return HTTP Response
# Create your views here.
