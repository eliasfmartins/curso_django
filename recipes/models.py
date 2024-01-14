from django.db import models
from django.contrib.auth.models import User
#tabela no banco de dados

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=65)
   
    def __str__ (self):
       return self.name
   #faz aparecer o nome ao invez de obj(id)


class  Recipe(models.Model):
    title = models.CharField(max_length=65)
    #campo do tipo string com no max 65 caracteres
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time =models.IntegerField(default=0)
    preparation_time_unit =models.CharField(default='',max_length=50)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=200)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(Category, on_delete =models.SET_NULL, null=True,blank=True, default=None)
    author = models.ForeignKey(User, on_delete =models.SET_NULL, null=True )
    
    def __str__(self):
        return self.title
    #quando deletar category vai settar o campo para null o null por padrao nao e aceito
    # esse null = True quer dizer  q aceita o campo receber valor Null