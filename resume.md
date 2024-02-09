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

## Populando templates utilizando func e for

Primeiro, vamos configurar o **Faker** em seu projeto Django. Certifique-se de que você já instalou a biblioteca usando o comando:

```bash
pip install Faker
```

Agora, vamos criar uma função que retorna um dicionário com dados fictícios. Vou chamá-la de `gerar_dados_ficticios()`:

```python
# myapp/utils.py

from faker import Faker

def gerar_dados_ficticios():
    fake = Faker()
    return {
        'title': fake.sentence(),
        'text': fake.paragraph(),
        'author': fake.name(),
        'published_date': fake.date(),
    }
```

Essa função cria um dicionário com chaves como `'title'`, `'text'`, `'author'` e `'published_date'`, preenchendo cada valor com dados fictícios gerados pelo  **Faker** .

Agora, na sua view, você pode usar essa função para criar uma lista de exemplos:

```python
# myapp/views.py

from django.shortcuts import render
from .utils import gerar_dados_ficticios

def home(request):
    exemplos = [gerar_dados_ficticios() for _ in range(10)]
    return render(request, 'template.html', {'exemplos': exemplos})
```

Na sua template (`template.html`), você pode iterar sobre os exemplos usando o loop `{% for exemplo in exemplos %}`:

```html
<!-- template.html -->

{% for exemplo in exemplos %}
    <h2>{{ exemplo.title }}</h2>
    <div>{{ exemplo.text }}</div>
    <p>Author: {{ exemplo.author }}</p>
    <p>Published Date: {{ exemplo.published_date }}</p>
{% endfor %}
```

Dessa forma, sua view renderizará o template com 10 exemplos de dados fictícios, que você pode usar para popular os cards no seu projeto Django. Lembre-se de adaptar os campos e as chaves do dicionário conforme necessário para o seu caso específico. 🚀

## URLs Dinâmicas no Django

Para utilizar URLs dinâmicas no Django, siga os passos abaixo:

1. **Definindo Nomes para as URLs** :

* Primeiramente, é necessário atribuir nomes às suas URLs no arquivo `urls.py`.
* Por exemplo:
  ```python
  urlpatterns = [
      path('', views.home, name="recipes-home"),
      path('recipes/<int:id>/', views.recipe, name="recipes-recipe"),
  ]
  ```

1. **Usando os Nomes das URLs nos Templates** :

* No seu template HTML, utilize a tag `{% url 'nome_da_url' %}` para chamar a URL pelo nome.
* Por exemplo, para criar um link para a página inicial:
  ```html
  <a href="{% url 'recipes-home' %}">Ir para a página inicial</a>
  ```

1. **Passando Parâmetros** :

* Caso a rota necessite de algum parâmetro, como um ID, você deve enviá-lo após o nome da rota.
* Por exemplo, para a URL `recipes-recipe`, você pode usar:
  ```html
  <a href="{% url 'recipes-recipe' id=42 %}">Ver receita</a>
  ```

1. **Utilizando o `app_name`** :

* É possível definir um `app_name` no arquivo `urls.py` do seu aplicativo.
* Por exemplo:
  ```python
  app_name = 'exemplo'

  urlpatterns = [
      path('', views.home, name="home"),
      path('recipes/<int:id>/', views.recipe, name="recipe"),
  ]
  ```
* Agora, na hora de chamar a URL, você pode usar:
  ```html
  <a href="{% url 'exemplo:home' %}">Ir para a página inicial</a>
  ```

Lembre-se de que os templates são poderosas ferramentas para criar interfaces interativas e personalizadas em suas aplicações Django. 🚀

Claro! Vou formatar o texto para você. Aqui está a versão organizada:

# Django Models e ORM (Object Relational Mapper)

No Django, um **modelo** basicamente representa uma tabela no banco de dados. O Django converte esses modelos em tabelas na base de dados.

Para criar seus modelos Django, você deve definir classes no arquivo `models.py` dentro do seu aplicativo (app).

Aqui está um exemplo de como criar um modelo:

```python
from django.db import models
from django.contrib.auth.models import User  # Importando o modelo User pra usar como tabela

class Category(models.Model):
    name = models.CharField(max_length=65)  # Nome da categoria

class Recipe(models.Model):
    title = models.CharField(max_length=65)  # Título da receita (campo de texto com no máximo 65 caracteres)
    description = models.CharField(max_length=165)  # Descrição da receita
    slug = models.SlugField()  # Campo especial para slugs (URLs amigáveis)
    preparation_time = models.IntegerField()  # Tempo de preparo em minutos (número inteiro)
    preparation_time_unit = models.CharField(max_length=65)  # Unidade de tempo (por exemplo, "minutos")
    serving_time = models.IntegerField()  # Tempo de servir em minutos (número inteiro)
    serving_unit = models.CharField(max_length=65)  # Unidade de tempo para servir (por exemplo, "minutos")
    preparation_steps = models.TextField()  # Passos de preparo (texto longo)
    preparation_steps_is_html = models.BooleanField(default=False)  # Indica se os passos de preparo contêm HTML
    created_at = models.DateTimeField(auto_now_add=True)  # Data e hora de criação (automática)
    updated_at = models.DateTimeField(auto_now=True)  # Data e hora de atualização (automática)
    is_published = models.BooleanField(default=False)  # Indica se a receita está publicada
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')  # Imagem de capa (local e formato do nome do arquivo)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # Relação com a tabela Category
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Relação com a tabela User
```

usando o aultor do proprio django ao invez de criar uma tabelha pros  autores importa se

from django.contrib.auth.models impor User esse user e um model

* `CharField`: Armazena texto com um limite de caracteres.
* `SlugField`: Usado para criar URLs amigáveis (slugs) a partir do título.
* `IntegerField`: Armazena números inteiros (como tempos de preparo e servir).
* `TextField`: Armazena texto longo (como os passos de preparo).
* `BooleanField`: Armazena valores verdadeiro/falso (como a publicação da receita).
* `DateTimeField`: Armazena data e hora (criação e atualização).
* `ImageField`: Armazena imagens de capa, com local e formato personalizados.
* `ForeignKey`: Cria uma relação entre tabelas (no caso, com as tabelas `Category` e `User`).
* `User`: O modelo padrão do Django para gerenciar usuários.

## Pillow e campos de imagem:

* O **Pillow** é uma biblioteca Python para processamento de imagens.
* Quando você usa o campo `ImageField` no Django (para armazenar imagens), o Pillow é necessário.
* Se o Pillow não estiver instalado, você receberá um erro ao executar as migrações.
* Para instalar o Pillow, você pode usar o seguinte comando:
  ```
  pip install pillow
  ```

Lembre-se de sempre rodar `makemigrations` após fazer alterações nos modelos e, em seguida, aplicar essas mudanças com `migrate`. Isso garante que seu banco de dados esteja sempre atualizado com a estrutura dos modelos.

## Migrations no Django: makemigrations e migrate

Quando você trabalha com o Django e cria ou altera modelos (models), é necessário aplicar essas mudanças ao banco de dados. Para isso, utilizamos os comandos `makemigrations` e `migrate`.

1. **`makemigrations`** :

* O comando `makemigrations` é usado **sempre que você faz alterações em um modelo** (adiciona, remove ou modifica campos).
* Ele cria um arquivo de migração que descreve as alterações feitas no modelo.
* Esse arquivo é salvo na pasta `migrations` dentro do seu aplicativo (app).
* Por exemplo, se você adicionou uma nova coluna à sua tabela, o `makemigrations` criará um arquivo que registra essa alteração.

1. **`migrate`** :

* O comando `migrate` é usado para  **aplicar essas mudanças diretamente ao banco de dados** .
* Ele executa as migrações pendentes (ou seja, as alterações registradas nos arquivos de migração) no banco de dados.
* Isso significa que as tabelas são criadas, modificadas ou excluídas conforme necessário.
* Por exemplo, se você adicionou uma nova coluna, o `migrate` criará essa coluna na tabela correspondente no banco de dados.

### Área Administrativa do Django

1. **Acessando a Área Administrativa** :

* Acesse o endereço `127.0.0.1:8000/admin` no seu navegador.
* Você precisará fazer login com um usuário e senha.

1. **Criando um Superusuário** :

* Para criar um superusuário, execute o seguinte comando no terminal:
  ```
  python manage.py createsuperuser
  ```
* Informe um nome de usuário, um email e uma senha.
* Esse superusuário será usado para fazer login na área administrativa.

1. **Tabelas Padrão** :

* Após fazer login, você verá duas tabelas padrão: `Groups` e `Users`.
* Você pode dar permissões a grupos de usuários e cadastrar novos usuários por meio dessas tabelas.

### Exibindo Tabelas Criadas na Área Administrativa

1. **Configuração no `admin.py`** :

* Para exibir as tabelas que você criou na área administrativa, vá para o arquivo `admin.py` do seu aplicativo.
* Crie uma classe para cada modelo (tabela) que deseja disponibilizar na área administrativa.
* Essa classe deve herdar de `admin.ModelAdmin`.
* Por exemplo, se você tem um modelo chamado `Category`, crie uma classe `CategoryAdmin`.

1. **Registro do Modelo** :

* No mesmo arquivo `admin.py`, registre o modelo com a classe administrativa:
  ```python
  from django.contrib import admin
  from .models import Category

  class CategoryAdmin(admin.ModelAdmin):
      # Configurações adicionais, se necessário

  admin.site.register(Category, CategoryAdmin)
  ```

1. **Personalizando a Exibição** :

* Por padrão, os itens na tabela serão exibidos como “Nome da Classe” + “object” (número de ID).
* Para exibir os nomes dos itens, adicione um método `__str__` ao seu modelo (em `models.py`):
  ```python
  class Category(models.Model):
      name = models.CharField(max_length=65)

      def __str__(self):
          return self.name
  ```
* Agora, os dados na tabela serão mostrados pelos nomes em vez de “object” + ID.



criando outra tabela


```python
from django.contrib import admin
from .models import Category, Recipe

class CategoryAdmin(admin.ModelAdmin):
    # Configurações adicionais, se necessário

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # Configurações adicionais, se necessário

admin.site.register(Category, CategoryAdmin)
```

essa e a segunda forma de publicar a sua tabela na area adm

### Alterando caminho das imagens salvas

mesmo com a configuracao  do campo cover as imagens estao sendo salvas dentro do app

para salvar as imagens dentro de uma pasta media na rais do projeto e preciso configurar o djando da seguinte forma

na settins.py do app

proximo as configuracoes de STATIC_ROOT

adicionar configuracao de MEDIA

MEDIA_URL= '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

a pasta onde sera salvo os arquivos enviados pelos usuarios

ainda assim quando vc cadastra uma imagem na parte adm do django ele disponibiliza um url pra vc poder acessala este nao estara funcionado  pois o django nao esta servindo esses arquivos

para configurar isso vc vai na pasta urls.py do app

vc faz uma concatenacao do seu urlpatterns ex:

from django.conf.url.static import static

from django.conf import settings

obs: esse MEDIA_URL e o  aquivo que foi configurado anteriormente

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

com essas configuracoes o django agora podera servir as imagens que ele recebeu dos ususarios
