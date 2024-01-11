from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price', 'category_id']
        
        
class CategoryForm(forms.ModelForm):
    
    class Meta:
        
        model = Category
        fields = ['category_name']
        
        
class MiFormulario(forms.Form):
    texto = forms.CharField(max_length=100)