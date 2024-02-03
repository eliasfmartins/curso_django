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

# Organização de Componentes no Django

Ao trabalhar com Django, é uma prática comum separar os componentes em diferentes diretórios para facilitar a organização e manutenção do código. Aqui estão algumas convenções sugeridas:

## Estrutura de Pastas

- **Partials:** Utilizada para armazenar componentes reutilizáveis.
- **Pages:** Destinada a conter os componentes específicos de cada página.

## Criando Componentes

**Partials:**

- Por convenção, crie uma pasta chamada `partials`.
- Dentro dessa pasta, organize os componentes de acordo com sua funcionalidade.

Exemplo:

/recipes

/partials

- head.html
- navbar.html
- footer.html

**Pages:**

- Crie uma pasta chamada `pages` para armazenar os componentes específicos de cada página.

Exemplo:

/recipes
/pages

- home.html
- about.html
- contact.html

## Incluindo Componentes nas Páginas

Para incluir componentes em suas páginas, utilize a tag `{% include %}`.

Exemplo de uso em um arquivo de template:

```
{% include 'recipes/partials/head.html' %}
```

Certifique-se de fornecer o caminho correto para o componente desejado. Essa abordagem facilita a manutenção e reutilização de componentes em diferentes partes do projeto.


## Arquivos estaticos

primeiro passo separe seu arquivo css ou javascript ou imagem

o servidor do django ja vem configurado para ler arquivos estaticos dentro da pasta do app por

padrao ele busca dentro da pasta static dentro da pasta static cria a mesma pasta com nome do app pra evitar colisao de nomes e dentro dessa pasta crio uma pasta pra alocar o css 

e necessario configurar a settings q ficam dentro do projeto em instaled app e preciso ter  'django.contrib.staticfiles', pra indicar pra ele buscar por aquivos estaticos geralmente ja vem por padrao

no arquivo que e necessario inportar o css ou arquivo desejado vc cria um link para static files

no topo do arquivo usa se uma tag {%load static%} pra indicar que ele deve carregart arquivos estaticos

exp de como ficaria o link for css

```javascript

<Link rel = 'stylesheet' href="{% static 'recipes/css/styles.css %}" ><>
```

a mesma coisa usa se o caminho para o arquivo depois da pasta static
