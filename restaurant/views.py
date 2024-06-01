from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido, ItemMenu, Cliente, Empleado, Pago, Inventario, ItemPedido
from .forms import PedidoForm, ItemPedidoForm, PagoForm, InventarioForm
from django.utils.dateparse import parse_date

def index(request):
    return render(request, 'restaurant/index.html')

def crear_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            return redirect('detalles_pedido', pk=pedido.pk)
    else:
        form = PedidoForm()
    return render(request, 'restaurant/crear_pedido.html', {'form': form})

def detalles_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    items = ItemPedido.objects.filter(pedido=pedido)
    return render(request, 'restaurant/detalles_pedido.html', {'pedido': pedido, 'items': items})

def gestionar_inventario(request):
    inventario = Inventario.objects.all()
    return render(request, 'restaurant/gestionar_inventario.html', {'inventario': inventario})

def gestionar_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'restaurant/gestionar_pagos.html', {'pagos': pagos})

def agregar_pago(request):
    if request.method == "POST":
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestionar_pagos')
    else:
        form = PagoForm()
    return render(request, 'restaurant/agregar_pago.html', {'form': form})

def editar_pago(request, pk):
    pago = get_object_or_404(Pago, pk=pk)
    if request.method == "POST":
        form = PagoForm(request.POST, instance=pago)
        if form.is_valid():
            form.save()
            return redirect('gestionar_pagos')
    else:
        form = PagoForm(instance=pago)
    return render(request, 'restaurant/editar_pago.html', {'form': form})

def eliminar_pago(request, pk):
    pago = get_object_or_404(Pago, pk=pk)
    if request.method == "POST":
        pago.delete()
        return redirect('gestionar_pagos')
    return render(request, 'restaurant/eliminar_pago.html', {'pago': pago})

def generar_reportes(request):
    pedidos = Pedido.objects.all()
    pagos = Pago.objects.all()
    
    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        
        if start_date:
            pedidos = pedidos.filter(fecha__gte=parse_date(start_date))
            pagos = pagos.filter(fecha__gte=parse_date(start_date))
        
        if end_date:
            pedidos = pedidos.filter(fecha__lte=parse_date(end_date))
            pagos = pagos.filter(fecha__lte=parse_date(end_date))
    
    return render(request, 'restaurant/generar_reportes.html', {'pedidos': pedidos, 'pagos': pagos})

def crear_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            return redirect('detalles_pedido', pk=pedido.pk)
    else:
        form = PedidoForm()
    return render(request, 'restaurant/crear_pedido.html', {'form': form})

def detalles_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    items = ItemPedido.objects.filter(pedido=pedido)
    return render(request, 'restaurant/detalles_pedido.html', {'pedido': pedido, 'items': items})

def gestionar_inventario(request):
    inventario = Inventario.objects.all()
    return render(request, 'restaurant/gestionar_inventario.html', {'inventario': inventario})

def gestionar_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'restaurant/gestionar_pagos.html', {'pagos': pagos})

def generar_reportes(request):
    pedidos = Pedido.objects.all()
    return render(request, 'restaurant/generar_reportes.html', {'pedidos': pedidos})

def agregar_inventario(request):
    if request.method == "POST":
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestionar_inventario')
    else:
        form = InventarioForm()
    return render(request, 'restaurant/agregar_inventario.html', {'form': form})

def editar_inventario(request, pk):
    item_inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == "POST":
        form = InventarioForm(request.POST, instance=item_inventario)
        if form.is_valid():
            form.save()
            return redirect('gestionar_inventario')
    else:
        form = InventarioForm(instance=item_inventario)
    return render(request, 'restaurant/editar_inventario.html', {'form': form})

def eliminar_inventario(request, pk):
    item_inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == "POST":
        item_inventario.delete()
        return redirect('gestionar_inventario')
    return render(request, 'restaurant/eliminar_inventario.html', {'item_inventario': item_inventario})