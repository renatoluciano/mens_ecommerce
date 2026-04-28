from django.shortcuts import render
from .models import Product

def product_list(request):
    # Busca todos os produtos por categoria salvos no banco de dados
    products = Product.objects.all().order_by('category')

    # Envia a lista de produtos para a página HTML renderizar
    return render(request, 'products/product_list.html', {'products': products})
