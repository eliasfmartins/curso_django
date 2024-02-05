# Configuração do Ambiente Virtual

* Para criar a venv: `python3 -m venv 'nome da venv'`
* Para ativar a venv: `source venv/bin/activate`

# Iniciar Projeto Django

* Execute o comando `django-admin startproject 'nome do projeto' .` (Não esqueça do ponto no final)
* Crie o arquivo de requisitos: `pip freeze > requirements.txt`
* Instale os requisitos: `pip install -r requirements.txt`

## Arquivos Principais

* Os arquivos `asgi.py` e `wsgi.py` são usados para desenvolvimento.
* O arquivo `__init__.py` é usado para modularizar arquivos Python.
* Os arquivos principais são `settings.py` e `urls.py`.

## URLs e Views

* As URLs recebem uma rota (`'/alguma rota'`) e uma view.
* A view é uma função que recebe uma request ou response e retorna uma resposta HTTP.
* Exemplo de uso: `HttpResponse('retorna uma string aqui')`.

## App com Django

* Para criar um app Django, execute: `python manage.py startapp 'nome do app'`.
* O arquivo `__init__.py` indica que a pasta é um pacote.
* O arquivo `apps.py` contém o nome do app e o caminho do banco de dados.
* O arquivo `models.py` define as tabelas do banco de dados.
* O arquivo `views.py` contém as views (sempre use o caminho completo nas importações).

## URLs e Rotas

* Crie um arquivo `urls.py` dentro da pasta do app.
* Exemplo de `urlpatterns`:
  ```python
  from django.urls import path, include

  urlpatterns = [
      path('', include('nome do app.urls')),
  ]
  ```
* Separar as URLs ajuda a organizar e incluir sub-rotas.

## Templates

* Use `render` em vez de `HttpResponse` para renderizar templates.
* Exemplo: `render(request, 'caminho/template.html')`.
* Crie uma pasta `templates` dentro do app para armazenar os templates.
* Configure em `settings.py` para reconhecer os templates do app.

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

* É possível passar dados para dentro do template usando variáveis e tags do Django. Certifique-se de explorar essa funcionalidade para tornar seus templates dinâmicos e interativos! 😊
* Você pode passar dados para dentro do template utilizando `context={dados}`.
* Exemplo de uso em `views.py`:

  ```python
  render(request, 'caminho/template', context={'teste': 'respostadoteste'})
  ```
* No template, utilize `{{teste}}` para acessar os dados passados.

# Organização de Componentes no Django

Ao trabalhar com Django, é uma prática comum separar os componentes em diferentes diretórios para facilitar a organização e manutenção do código. Aqui estão algumas convenções sugeridas:

## Estrutura de Pastas

* **Partials:** Utilizada para armazenar componentes reutilizáveis.
* **Pages:** Destinada a conter os componentes específicos de cada página.

## Criando Componentes

**Partials:**

* Por convenção, crie uma pasta chamada `partials`.
* Dentro dessa pasta, organize os componentes de acordo com sua funcionalidade.

Exemplo:

```
/recipes
/partials
  - head.html
  - navbar.html
  - footer.html
```

**Pages:**

* Crie uma pasta chamada `pages` para armazenar os componentes específicos de cada página.

Exemplo:

```
/recipes
/pages
  - home.html
  - about.html
  - contact.html
```

## Incluindo Componentes nas Páginas

Para incluir componentes em suas páginas, utilize a tag `{% include %}`.

Exemplo de uso em um arquivo de template:

```
{% include 'recipes/partials/head.html' %}
```

Certifique-se de fornecer o caminho correto para o componente desejado. Essa abordagem facilita a manutenção e reutilização de componentes em diferentes partes do projeto.

Lembre-se de explorar essas práticas para criar templates bem organizados e reutilizáveis em seus projetos Django! 😊

## Arquivos Estáticos

Ao lidar com arquivos estáticos, como CSS, JavaScript ou imagens, o Django facilita o processo de configuração e utilização.

### Configuração Inicial

1. **Separe os Arquivos:**

   * Separe seus arquivos CSS, JavaScript ou imagens em uma pasta específica.
2. **Configuração Padrão do Django:**

   * O servidor do Django já está configurado para ler arquivos estáticos dentro da pasta do aplicativo.
   * Por padrão, ele busca na pasta `static`. Dentro dessa pasta, é uma prática criar uma subpasta com o nome do aplicativo para evitar colisões de nomes.
     ```
     /recipes
         /static
             /recipes
                 /css
                     - styles.css
     ```
3. **Configuração no Settings:**

   * No arquivo `settings.py` do projeto, verifique se `'django.contrib.staticfiles'` está presente em `INSTALLED_APPS`.
   * Isso indica ao Django para buscar arquivos estáticos.

   Exemplo:

   ```python
   INSTALLED_APPS = [
       # ...
       'django.contrib.staticfiles',
   ]
   ```

### Utilizando Arquivos Estáticos nos Templates

1. **Importando na Página:**

   * No arquivo onde deseja importar o CSS ou outro arquivo estático, use a tag `{% load static %}` no topo para indicar que os arquivos estáticos devem ser carregados.
2. **Exemplo de Uso:**

   * Para criar um link para um arquivo CSS, use o seguinte formato:
     ```html
     <link rel="stylesheet" href="{% static 'recipes/css/styles.css' %}">
     ```
   * Certifique-se de incluir o caminho a partir da pasta `static`.

   <link rel=“stylesheet” href=“{% static ‘recipes/css/styles.css’ %}”>

## Configuração de Diretórios para Arquivos Estáticos

Ao lidar com arquivos estáticos que não estão diretamente atrelados a nenhum aplicativo específico, é comum criar uma pasta global para evitar conflitos de nome. Vamos chamar essa pasta de `base_static`.

1. **Criando a Estrutura:**

   * Crie uma pasta chamada `base_static`.
   * Dentro dela, organize os arquivos estáticos, por exemplo, em uma subpasta `css`.

   Exemplo:

   ```
   /base_static
       /css
           - styles.css
   ```

### Configuração no Settings

1. **Configurando o Settings.py:**

   * Adicione a chave `STATICFILES_DIRS` em `settings.py` para indicar ao Django onde procurar esses arquivos estáticos globais.

   Exemplo:

   ```python
   STATICFILES_DIRS = [BASE_DIR / 'base_static']
   ```

### Utilizando Arquivos Estáticos Globais nos Templates

1. **Linkando o CSS:**

   * Ao linkar um arquivo CSS global, certifique-se de usar o caminho correto. Utilize a tag `{% static %}` da seguinte maneira:

     ```html
     <link rel="stylesheet" href="{% static 'global/css/styles.css' %}">
     ```
   * **Namespace:**

     * É útil adicionar um namespace para evitar conflitos. Isso significa que, ao usar um arquivo estático global, o prefixo `global/` é recomendado para garantir um caminho único.

     Exemplo:

     ```html
     <link rel="stylesheet" href="{% static 'global/css/styles.css' %}">
     ```

   Ao seguir essas práticas, o Django procurará arquivos estáticos nos diretórios configurados em `STATICFILES_DIRS`, permitindo o uso de arquivos estáticos globais em sua aplicação.

## Coletando Arquivos Estáticos da Aplicação

   Para reunir todos os arquivos estáticos de sua aplicação, utilize o comando:

```bash
   python manage.py collectstatic
```

### Configuração do `STATIC_ROOT`

1. **Configuração no `settings.py`:**

   * Antes de executar o comando `collectstatic`, é necessário configurar o `STATIC_ROOT` no arquivo `settings.py` do aplicativo.

   Exemplo:

   ```python
   STATIC_ROOT = BASE_DIR / 'static'
   ```

   Essa configuração informa ao Django onde salvará todos os arquivos estáticos coletados.

### Importância do Namespace

* **Evitando Conflitos:**

  * O uso de namespaces, como mencionado anteriormente (`global/`), é crucial ao coletar arquivos estáticos.
  * Quando você executa o comando `python manage.py collectstatic`, ele reúne todos os arquivos estáticos de todas as aplicações e os coloca na pasta configurada em `STATIC_ROOT`.
  * O namespace garante que arquivos com o mesmo nome, mas provenientes de diferentes aplicativos, não entrem em conflito.

  Ao seguir essas etapas, você pode garantir uma coleta adequada de todos os arquivos estáticos de sua aplicação, evitando conflitos e mantendo a organização. 😊

# URLs Dinâmicas com Django

Quando trabalhamos com URLs em um projeto Django, é importante entender como configurá-las corretamente para que a aplicação possa rotear as solicitações do usuário para as views apropriadas. Vamos abordar alguns conceitos essenciais relacionados a URLs dinâmicas.

## Importando Views

Em vez de importar uma view de cada vez, podemos importar toda uma pasta. Por exemplo, suponha que temos uma pasta chamada “recipes” com um arquivo de views. Podemos fazer o seguinte importe:

```python
from recipes import views
```

Isso significa que estamos importando o arquivo “views.py” da pasta “recipes”. Lembre-se de que, em vez de usar a função diretamente, devemos referenciar a view como `views.nome_da_funcao`.

## Configurando uma Nova URL

Ao criar uma nova URL, precisamos configurar uma view para determinar o que será exibido na rota específica. Por exemplo, suponha que queremos criar uma rota chamada “/receita/”.

Primeiro, criamos a view correspondente:

```python
def recipe(request):
    return render(request, 'nomedotemplate.html', context={'teste': 'teste'})
```

Agora podemos implementar a nova URL no arquivo `urls.py`:

```python
urlpatterns = [
    path('', views.home),
    path('receita/', views.recipe),
]
```

## Parâmetros em URLs Dinâmicas

Quando lidamos com URLs dinâmicas, muitas vezes precisamos receber parâmetros na URL e passá-los para a view. Por exemplo, podemos criar uma URL que espera um parâmetro chamado “id”:

```python
path('receita/<int:id>/', views.recipe)
```

Nesse exemplo, o valor do parâmetro “id” será extraído diretamente da URL e passado para a view. É importante que a view declare esse parâmetro para acessar o valor:

```python
def recipe(request, id):
    # Faça algo com o valor de "id"
    return render(request, 'nomedotemplate.html', context={'teste': 'teste'})
```

Além do tipo “int”, existem outros tipos de parâmetros, como “slug”, “uuid” e outros, que podem ser usados conforme necessário.

# Blocos em Templates do Django

Ao trabalhar com templates no Django, é importante evitar a repetição de código e manter uma estrutura organizada. Uma maneira de fazer isso é usando um  **base template** , que carrega o HTML comum a todas as páginas e permite substituir apenas o conteúdo específico de cada página.

## Base Template

O base template contém a estrutura geral do site, incluindo o cabeçalho e o rodapé. O “miolo” da página, que varia entre as diferentes páginas, será substituído. Para isso, utilizamos a tag `{% block content %} {% endblock content %}`.

## Como Funciona

1. **Crie um Base Template** : Crie um arquivo de template que servirá como base para todas as páginas. Nesse arquivo, defina os elementos comuns a todas as páginas, como o cabeçalho e o rodapé.
2. **Defina Blocos no Base Template** : Dentro do base template, utilize a tag `{% block content %}` para indicar onde o conteúdo específico de cada página será inserido. Por exemplo:

```html
   <!DOCTYPE html>
   <html>
   <head>
       <!-- Meta tags, CSS, etc. -->
   </head>
   <body>
       <header>
           <!-- Cabeçalho comum a todas as páginas -->
       </header>
       <div class="content">
           {% block content %}
           <!-- Conteúdo específico da página -->
           {% endblock content %}
       </div>
       <footer>
           <!-- Rodapé comum a todas as páginas -->
       </footer>
   </body>
   </html>
```

1. **Páginas Específicas (Componente Page)** : Crie arquivos de template para cada página específica. Esses arquivos herdarão do base template e conterão apenas o conteúdo único de cada página. Por exemplo:

```html
   {% extends 'global/base.html' %}

   {% block content %}
       <!-- Conteúdo específico da página -->
       <h1>Minha Página</h1>
       <p>Texto da página...</p>
   {% endblock content %}
```

Dessa forma, o conteúdo dentro do bloco `{% block content %}` no componente page substituirá o conteúdo correspondente no base template. Isso mantém a estrutura organizada e evita repetições desnecessárias.

Claro! Vamos ajustar o seu resumo e melhorar o que for possível:

## Título Dinâmico em Templates do Django

Para criar um título dinâmico nos templates do Django, siga estas etapas:

1. **Configuração Inicial:**
   * No arquivo `base.html`, adicione as seguintes linhas no início do documento:
     ```html
     <!DOCTYPE html>
     <html lang="pt-BR">
     ```
   * Em seguida, inclua o conteúdo do arquivo `head.html` usando a tag `{% include 'head.html' %}`. Isso garantirá que os links de CSS, fontes e outros recursos sejam carregados corretamente.
2. **Título Dinâmico:**
   * Dentro da tag `<head>`, adicione uma tag `<title>` e defina o valor como um bloco. Por exemplo:
     ```html
     <title>{% block title %}Título Padrão{% endblock title %}</title>
     ```
   * Certifique-se de que o bloco `title` esteja definido nos templates específicos (como `index.html` ou outras páginas).

Dessa forma, você pode criar títulos dinâmicos para suas páginas usando blocos no Django. Lembre-se de substituir o valor padrão pelo título específico de cada página. 😊

e possivel gerar uma funcao com a biblioteca faker para retorna um dicionario com dados ficticios e executar essa funcao pra usar como contexto e popular cards no caso de receitas 

e na view que renderiza o template passar como contexto exemplo

def home(request):

    return render(request, 'tempate/template.html', context{ ' exemplo':[nome_funcao() for_ in  range(10)})

basicamente vai executar a funcao 10x e gerar obj
