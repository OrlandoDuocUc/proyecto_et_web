from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import local_list, local_create, local_update, local_delete


#nuevas importaciones
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    #nueva hoja html
    path('productos_new/', views.productos_new, name='productos_new'),
    
    #dirigir a sobre_nosotros
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    
    # estas dos path nos ayudan a gestionar el login
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    
    path('logout/', views.logout_view, name='logout'),
    
    path('productos', views.lista_productos, name='productos'),
    
    # esta pagina es la TIENDA DE PRODUCTOS
    path('empezar', views.empezar, name="empezar"),
    
    # esta es la vista donde CREAMOS, BORRAMOS, ELIMINAMOS PRODUCTOS
    path('edit', views.edit, name='edit'), # esta vista es importante porque es el panel administrador (solo admin).
    
    path('edit/crear', views.crear_producto, name='crear'),
    path('edit/editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
        
    # esto seria el crud
    path('carro/agregar/<int:producto_id>/', views.agregar_producto, name='agregar_producto'),
    path('carro/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('carro/restar/<int:producto_id>/', views.restar_producto, name='restar_producto'),
    path('carro/sumar/<int:producto_id>/', views.sumar_producto, name='sumar_producto'),
    path('carro/limpiar/', views.limpiar_carrito, name='limpiar_carrito'),
    
    # boton para que se agregue un producto al carro.
    path('agregar_al_carro/<int:producto_id>/', views.agregar_al_carro, name='agregar_al_carro'),
    
    # ESTE ES MI CARRITO DE COMPRAS DONDE PUEDO AGREGAR MAS PRODUCTOS O IR A PAGAR (CLIENTE)
    path('carro/tienda', views.tienda, name='tienda'),
    
    # pagina de pago, esta pagina gestiona nuestro pago una vez que apretamos en "Proceder al pago"
    path('checkout/', views.checkout, name='checkout'),
    
    # urls de CRUD PROVEEDORES
     path('proveedores/', views.proveedor_list, name='proveedor_list'),
    path('proveedores/nuevo/', views.proveedor_create, name='proveedor_create'),
    path('proveedores/editar/<int:pk>/', views.proveedor_update, name='proveedor_update'),
    path('proveedores/eliminar/<int:pk>/', views.proveedor_delete, name='proveedor_delete'), 
    
    # urls para locales
    path('locales/', local_list, name='local_list'),
    path('locales/nuevo/', local_create, name='local_create'),
    path('locales/editar/<int:pk>/', local_update, name='local_update'),
    path('locales/eliminar/<int:pk>/', local_delete, name='local_delete'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

