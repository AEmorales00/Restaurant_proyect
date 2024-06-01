from django import forms
from .models import Pedido, ItemPedido, Pago, Inventario

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente',  'estado']

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['item_menu', 'cantidad']

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['pedido', 'monto']

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['item_menu', 'cantidad']