from django.db import models
#tabela no banco de dados
# Create your models here.

class  Recipe(models.Model):
    title = models.CharField(max_length=65)
    #campo do tipo string com no max 65 caracteres
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=200)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')