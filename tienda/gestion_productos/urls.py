from django.urls import path
from .views import MiPrimeraVista, DetailsView, ProductCreationView, FilterView, ProductsFilter, ProductsList

urlpatterns = [
    path('home/', MiPrimeraVista.as_view(), name='home' ),
    path('<int:id>', DetailsView.as_view(), name='details' ),
    path('form', ProductCreationView.as_view(), name='form' ),
    path('filter/<int:id>', FilterView.as_view(), name='filter' ),
    path('products/', ProductsList.as_view(), name='products' ),
    path('productsFilter/', ProductsFilter.as_view(), name='productsF' ),
]
