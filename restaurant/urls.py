from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pedido/crear/', views.crear_pedido, name='crear_pedido'),
    path('pedido/<int:pk>/', views.detalles_pedido, name='detalles_pedido'),
    path('inventario/', views.gestionar_inventario, name='gestionar_inventario'),
    path('inventario/agregar/', views.agregar_inventario, name='agregar_inventario'),
    path('inventario/editar/<int:pk>/', views.editar_inventario, name='editar_inventario'),
    path('inventario/eliminar/<int:pk>/', views.eliminar_inventario, name='eliminar_inventario'),
    path('pagos/', views.gestionar_pagos, name='gestionar_pagos'),
    path('pagos/agregar/', views.agregar_pago, name='agregar_pago'),
    path('pagos/editar/<int:pk>/', views.editar_pago, name='editar_pago'),
    path('pagos/eliminar/<int:pk>/', views.eliminar_pago, name='eliminar_pago'),
    path('reportes/', views.generar_reportes, name='generar_reportes'),
]