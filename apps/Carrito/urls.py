
from django.urls import path
from apps.Carrito.views import inicio, Tienda, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito

app_name = 'Tienda'

urlpatterns = [
    # ---------------------------------------------------------
    # TIENDA
    path('', inicio, name='index'),
    path('tienda/', Tienda, name='index'),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),

]
