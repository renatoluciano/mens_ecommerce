from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def product_list(request):
    # Busca todos os produtos por categoria salvos no banco de dados
    products = Product.objects.all().order_by('category')

    # Envia a lista de produtos para a página HTML renderizar
    return render(request, 'products/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    # Busca o produto pelo ID ou dá erro 404 se não existir
    product = get_object_or_404(Product, id=product_id)
    
    # Busca o carrinho na sessão atual do usuário, ou cria um vazio
    cart = request.session.get('cart', {})
    
    # Adiciona o produto ou aumenta a quantidade se já estiver lá
    product_id_str = str(product_id)
    if product_id_str in cart:
        cart[product_id_str]['quantity'] += 1
    else:
        cart[product_id_str] = {
            'name': product.name,
            'price': str(product.price),
            'quantity': 1
        }
        
    # Salva o carrinho atualizado de volta na sessão
    request.session['cart'] = cart
    
    return redirect('product_list')

def cart_detail(request):
    cart = request.session.get('cart', {})
    total_price = 0
    
    # Calcula o valor total do carrinho
    for item in cart.values():
        total_price += float(item['price']) * item['quantity']
        
    return render(request, 'products/cart_detail.html', {'cart': cart, 'total_price': total_price})
