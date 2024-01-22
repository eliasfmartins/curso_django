# Configuração do Ambiente Virtual

- Criar a venv: `python3 -m venv 'nome da venv'`
- Iniciar a venv: `source venv/bin/activate`

# Iniciar Projeto Django

- `django-admin startproject 'nome do projeto' .` (Não esqueça do ponto)
- Criar requisitos: `pip freeze > requirements.txt`
- Instalar requisitos: `pip install -r requirements.txt`

## Arquivos Principais

- `asgi.py` e `wsgi.py` são usados para desenvolvimento.
- `__init__.py` é usado para modularizar arquivos Python.
- Arquivos principais: `settings.py` e `urls.py`.

## URLs e Views

- A URL recebe uma rota (`'/alguma rota'`) e uma view.
- A view é uma função que recebe uma request ou response e retorna uma resposta HTTP.
- Exemplo de uso: `HttpResponse('retorna uma string aqui')`.

## App com Django

- Criar app Django: `python manage.py startapp 'nome do app'`.
- `__init__.py` indica que a pasta é um pacote.
- `apps.py` contém o nome do app e o caminho do banco de dados.
- `models.py` define as tabelas do banco de dados.
- `views.py` contém as views (sempre usar caminho completo nas importações).

## URLs e Rotas

- Criar arquivo `urls.py` dentro da pasta do app.
- Exemplo de `urlpatterns`:
  ```python
  from django.urls import path, include

  urlpatterns = [
      path('', include('nome do app.urls')),
  ]
  ```
- Separar as URLs ajuda a organizar e incluir sub-rotas.

## Templates

- Usar `render` em vez de `HttpResponse` para renderizar templates.
- Exemplo: `render(request, 'caminho/template.html')`.
- Criar uma pasta `templates` dentro do app para armazenar templates.
- Configurar em `settings.py` para reconhecer templates do app.

Exemplo em INSTALLED_APPS e TEMPLATES:

```python
INSTALLED_APPS = [
    # ...
    'nome do app',
]

TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'nome do app', 'templates')],
        # ...
    },
]
```


## Contexto

- É possível passar dados para dentro do template utilizando `context={dados}`.
- Exemplo de uso em `views.py`:
  ```python
  render(request, 'caminho/template', context={'teste': 'respostadoteste'})
  ```

* No template, utilize `{{teste}}` para acessar os dados passados.
