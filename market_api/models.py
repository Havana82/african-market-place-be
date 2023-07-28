from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(default="")
    
    
    def __str__(self) -> str:
        return self.name

   
    
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, default="")
    price = models.IntegerField(null=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
   
    