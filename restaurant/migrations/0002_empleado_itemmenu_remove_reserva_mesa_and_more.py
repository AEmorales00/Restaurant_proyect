# Generated by Django 5.0.6 on 2024-06-01 05:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('puesto', models.CharField(choices=[('mesero', 'Mesero'), ('cocinero', 'Cocinero'), ('cajero', 'Cajero'), ('administrador', 'Administrador'), ('gerente', 'Gerente')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ItemMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='mesa',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='mesa',
        ),
        migrations.RemoveField(
            model_name='ordencompra',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='cliente',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='fecha_pedido',
            new_name='fecha',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='fecha_actualizacion',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventario',
            name='cantidad',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('preparando', 'Preparando'), ('entregado', 'Entregado')], max_length=50),
        ),
        migrations.AddField(
            model_name='inventario',
            name='item_menu',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant.itemmenu'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('item_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.itemmenu')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='restaurant.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.pedido')),
            ],
        ),
        migrations.DeleteModel(
            name='DetallePedido',
        ),
        migrations.DeleteModel(
            name='Mesa',
        ),
        migrations.DeleteModel(
            name='OrdenCompra',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
    ]
