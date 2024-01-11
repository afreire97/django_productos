from django.shortcuts import render, redirect
from django.views import View
from .models import Category, Product
from .forms import ProductForm, CategoryForm, MiFormulario
# Create your views here.


class MiPrimeraVista(View):
    
    
    template_name = 'index.html'
    
    def get(self, request):
        
        lista_productos = Product.objects.all()
        lista_categorias = Category.objects.all()
        
        
        
        context = {
            
            'lista_productos': lista_productos,
            'lista_categorias': lista_categorias,
            
            
        }
        return render(request, self.template_name, context)

class DetailsView(View):
    
    template_name = 'details.html'
    
    
    def get(self, request, id):
        
        producto = Product.objects.get(id=id)
        
        
        context = {
            'producto': producto
        }
        
        return render(request, 'details.html', context)
    

class FilterView(View):
    
    template_name = 'filter.html'
    
    def get(self, request, id):
        
        
        categoria = Category.objects.get(pk=id)
        
        
        
        productos_por_categoria = Product.objects.all().filter(product_name__startswith="C", category_id=categoria.id)
        
        
        return render(request, self.template_name, {'productos': productos_por_categoria})
        
        
        
        
class ProductCreationView(View):
    
    template_name = 'form.html'
    form_class = ProductForm
    
    
    def get(self, request):
        
        form = self.form_class()
        
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        
        form = self.form_class(request.POST)
        
        if form.is_valid():
            
            new_product = form.save()
            
            
            
            return redirect('details', id=new_product.id)
        
        
class ProductsList(View):
    template_name = 'products.html'
    
    
    def get(self, request):
        
        lista = Product.objects.all()
        
        return render(request, 'products.html', {'lista': lista})
    
    
    
class ProductsFilter(View):
    
    
    template_name = 'products.html'
    


    def get(self, request):
        form = MiFormulario()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = MiFormulario(request.POST)
        if form.is_valid():
            texto = form.cleaned_data['texto']
            # Haz algo con la cadena, por ejemplo, imprímela en la consola
            products_filtered = Product.objects.all().filter(product_name__startswith=texto)
            # Aquí puedes redirigir a otra vista o hacer lo que necesites con la cadena
        return render(request, self.template_name, {'products': products_filtered})