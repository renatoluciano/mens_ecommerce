from django.urls import path
from . import views

urlpatterns = [
    # Quando o cliente acessar a raiz do app, ele cai na lista de produtos
    path('', views.product_list, name='product_list'),
]
