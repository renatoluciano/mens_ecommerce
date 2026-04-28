from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib import messages

def product_list(request):
    # Pega a categoria selecionada na URL (se houver)
    category_slug = request.GET.get('categoria')
    
    # Se houver categoria, filtra os produtos. Se não, traz todos.
    if category_slug:
        products = Product.objects.filter(category=category_slug)
    else:
        products = Product.objects.all()
        
    # Pega todas as categorias cadastradas sem repetição para montar o menu
    categories = Product.objects.values_list('category', flat=True).distinct()
        
    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'current_category': category_slug
    })

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
    
    # Calcula o subtotal de cada item e o total geral
    for item in cart.values():
        item['subtotal'] = float(item['price']) * item['quantity']
        total_price += item['subtotal']
        
    return render(request, 'products/cart_detail.html', {'cart': cart, 'total_price': total_price})


def clear_cart(request):
    # Verifica se existe um carrinho na sessão e o deleta
    if 'cart' in request.session:
        del request.session['cart']
        
    return redirect('cart_detail')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    
    # Se o produto estiver no carrinho, remove ele
    if product_id_str in cart:
        del cart[product_id_str]
        request.session['cart'] = cart
        
    return redirect('cart_detail')

def increase_quantity(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        cart[product_id_str]['quantity'] += 1
        request.session['cart'] = cart
        
    return redirect('cart_detail')

def decrease_quantity(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        # Se a quantidade for 1, remove o item por completo
        if cart[product_id_str]['quantity'] <= 1:
            del cart[product_id_str]
        else:
            cart[product_id_str]['quantity'] -= 1
            
        request.session['cart'] = cart
        
    return redirect('cart_detail')

def checkout(request):
    cart = request.session.get('cart', {})
    
    # 🛑 REGRA DE SEGURANÇA: Se o carrinho estiver vazio
    if not cart:
        messages.warning(request, "Seu carrinho está vazio! Adicione produtos antes de finalizar a compra.")
        return redirect('product_list')
        
    # Se tiver produtos, zera o carrinho
    del request.session['cart']
    
    # 🎉 MENSAGEM DE SUCESSO
    messages.success(request, "Compra finalizada com sucesso! Agradecemos a preferência.")
    
    return redirect('product_list')