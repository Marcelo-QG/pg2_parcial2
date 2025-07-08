from django.db import models

class PedidoCono(models.Model):
    cliente = models.CharField(max_length=100)
    variante = models.CharField(
        max_length=20,
        choices=[
            ('carnivoro', 'Carnívoro'),
            ('vegetariano', 'Vegetariano'),
            ('saludable', 'Saludable'),
        ]
    )
    toppings = models.JSONField(default=list)
    tamanio_cono = models.CharField(
        max_length=10,
        choices=[
            ('pequenio', 'Pequeño'),
            ('mediano', 'Mediano'),
            ('grande', 'Grande'),
        ]
    )
    fecha_pedido = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} - {self.variante} - {self.tamanio_cono}"
