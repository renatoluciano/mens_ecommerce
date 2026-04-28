from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclui as rotas do nosso app de roupas na página inicial do site
    path('', include('products.urls')),
]