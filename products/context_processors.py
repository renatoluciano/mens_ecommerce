def cart_counter(request):
    cart = request.session.get('cart', {})
    total_items = 0
    
    # Soma as quantidades de todos os produtos no carrinho
    for item in cart.values():
        total_items += item['quantity']
        
    return {'cart_total_items': total_items}
