from django.contrib import admin
from .models import Cliente, Pedido, ItemMenu, ItemPedido, Inventario, Empleado, Pago

# Registro de modelos para el panel de administración de Django

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email')
    search_fields = ('nombre', 'email')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha', 'estado')
    list_filter = ('estado', 'fecha')
    search_fields = ('cliente__nombre', 'estado')
    date_hierarchy = 'fecha'

@admin.register(ItemMenu)
class ItemMenuAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio')
    search_fields = ('nombre',)

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'item_menu', 'cantidad')
    list_filter = ('pedido', 'item_menu')

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('item_menu', 'cantidad')
    list_filter = ('item_menu',)
    search_fields = ('item_menu__nombre',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'puesto')
    list_filter = ('puesto',)
    search_fields = ('nombre', 'puesto')

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'monto', 'fecha')
    list_filter = ('fecha',)
    search_fields = ('pedido__cliente__nombre',)
    date_hierarchy = 'fecha'