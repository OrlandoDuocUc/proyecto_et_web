from django.contrib import admin
from django.urls import path, include
from Proyecto_Ap import views
from Proyecto_Ap.views import agregar_producto, eliminar_producto, limpiar_carrito, restar_producto

#nuevas importaciones
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Proyecto_Ap.urls')),
    path('agregar/<int:producto_id>/',agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/',eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/',restar_producto, name="Sub"),
    path('limpiar/<int:producto_id>/',limpiar_carrito, name="Cls"),
    
    #codigo nuevo
    path('api/', include(router.urls)),
]
