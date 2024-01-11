from django.db import models

# Create your models here.


class Category(models.Model):
    
    category_name = models.CharField(max_length=150)
    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    
    product_name = models.CharField(max_length=150)
    description = models.TextField(max_length=200, default='No description provided')
    price = models.FloatField()
    date = models.DateField(auto_now_add=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    




    def __str__(self):
        return self.product_name
    
