from django.shortcuts import render, redirect
from apps.Carrito.carrito import Carrito
from apps.Carrito.models import Producto


# ---------------------------------------------------------
# VIEWS TIENDA

def inicio(request):
    return render(request, "index.html")


def Tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos': productos})


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda:index")


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda:index")


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda:index")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda:index")
