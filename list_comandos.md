criar venv = python3 -m venv 'nome da venv'
django-admin startproject 'nomeproject' .
fazer o requirimests = pip freeze > requirements.txt
pra instalar o requirements =  pip install -r requirements.txt
pra ativar a venv = source venv/bin/activate // caminho da venv

## iniciar projeto Django

* django-admin startproject 'nome do projeto' + . nao esquecer do ponto

> django-admin so e usado pra startar o projeto literalmente ....

asgi.py and wsgi.py sao usados pra desenvolvimento

__init__.py e usado pra usar os arquivos o python como modulos  e etc

arquivos mais usados seram settings.py e url.py

a url recebe uma rota ('/alguma rota ', e uma view)

a view nada mais e doque uma função que recebe uma request ou  response e retorna

uma resposta http uma view por padrao ja recebe o request e deve retorna alguma coisa

no caso usei  o HttpResponse('retorna uma string aqui') lenbrando que isso e um methodo 

para enviar uma resposta http

o app e o coracao da aplicação e praticamente uma pasta onde vc coloca as suas urls da aplicação view templates a e demais coisas

## app com DJango

criando app no django utiliza -se python manage.py startapp 'name do app'

init.py so serve pra indicar ao python q a pasta e um pacote

apps.py tem o nome do seu app e caminho de banco de dados 

models sao as tabelas do banco de dados

views e  o arquivo onde voce criar asuas views

ao fazer as importacoes no django sempre usar o caminho completo

ex: ao invez de view colocar o nome do app from recipes.views import Home

## Urls rotas

tbm e importante separar as urls no caso dentro da pasta do app crie um novo arquivo urls.py

o arquivo geralmente sera assim


from django.urls import path, include# esse include e pra incluir



urlpatterns = [

path('', include('nome do app.urls))

vai incluir as urls de dentro de urls do app

dentro da string vazia vai virar o caminho no caso vai passar a url de dentro diretamente a partir

da '/' rais do site se eu colocasse 'pao' seria pao/urls e etc...

]

## Templates

o HttpREsponse era utilizado apenas pra fins de teste e renderizar texto

importa se o render

from django.shortcuts impoort render

o methodo render renderiza um template

ex: def home(request):

    return render(request, 'caminho/template.html)

em resumo vc passa a requisicao e o caminho do template

por convenção dentro do seu app vc cria uma pasta chamada template

### E preciso ir em configurações do projeto 

alterar configuracoes pra buscar informacoes dentro do app

caso o contrario ele n ira buscar o template dentro do seu app

em settings.py do projeto procurar INSTALLED_APPS

colocar o nome do seu app la dentro pra ele tomar ciencia da existencia do mesmo

no mesmo arquivo de configuracoes em TEMPLATES

na chave DIRS voce pode colocar os caminhos onde os templates serao buscados

o BASE_DIR pega o caminho da raiz do projeto  da rais voce coloca o caminho q ele 

deve procurar os templates o problema ocorre quando tem 2 arquivos com o mesmo

nome por isso e tbm uma convencao colocar dentro da pasta templates 

uma pasta com nome do app/nome_template.html

sempre q colocar o caminho da url com nome do app para nao haver colisao de nomes

pois o django pega o primeiro q ele achar
