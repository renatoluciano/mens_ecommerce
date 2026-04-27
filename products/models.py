from django.db import models

class Product(models.Model):
    # Definimos os tamanhos padrão masculinos
    SIZES = [
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
        ('GG', 'Extra Grande'),
    ]
    
    CATEGORIES = [
        ('Camisas', 'Camisas'),
        ('Calças', 'Calças'),
        ('Casacos', 'Casacos'),
        ('Acessórios', 'Acessórios'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=2, choices=SIZES)
    category = models.CharField(max_length=100, choices=CATEGORIES, default='Camisas')
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.size})"
