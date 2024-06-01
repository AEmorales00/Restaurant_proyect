from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    ESTADO_PEDIDO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=ESTADO_PEDIDO_CHOICES, default='pendiente')

    def __str__(self):
        return f"Pedido {self.pk} de {self.cliente.nombre}"

class ItemMenu(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='items', on_delete=models.CASCADE)
    item_menu = models.ForeignKey(ItemMenu, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

class Inventario(models.Model):
    item_menu = models.ForeignKey(ItemMenu, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=50, choices=[('mesero', 'Mesero'), ('cocinero', 'Cocinero'), ('cajero', 'Cajero'), ('administrador', 'Administrador'), ('gerente', 'Gerente')])

class Pago(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=6, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago de {self.monto} para el pedido {self.pedido.pk}"

def __str__(self):
    return f"{self.item_menu.nombre} - {self.cantidad}"