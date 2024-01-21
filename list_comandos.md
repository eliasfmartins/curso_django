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
