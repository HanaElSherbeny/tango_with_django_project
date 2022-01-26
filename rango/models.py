from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self): 
        return self.name
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    
    
    
class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    def __str__(self): 
        return self.title

class PageAdmin(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    list_display = ('title', 'category', 'url')

    def __str__(self): 
        return self.title