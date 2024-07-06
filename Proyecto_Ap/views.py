from django.shortcuts import render, redirect, get_object_or_404
from .Carrito_C import Carrito
from .models import productos, Proveedor, Local
from .forms import ProductosForm, ProveedorForm, LocalForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from .serializers import ProductoSerializer #importamos serializers
from rest_framework import viewsets #importamos viewset

#################################codigo para usar json y ajax
#codigo en base a serializers
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = productos.objects.all()
    serializer_class = ProductoSerializer

#nuevo
def productos_new(request):
    productos_list = productos.objects.all()
    return render(request, 'plantillas/productos_new.html', {'productos': productos_list})
  

#################################hasta aca llega el codigo nuevo

##### VISTAS CRUD PARA PROVEEDORES ######
# Vista para listar proveedores
@login_required
@user_passes_test(lambda u: u.is_staff)
def proveedor_list(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'plantillas/proveedor_list.html', {'proveedores': proveedores})

# Vista para crear un nuevo proveedor
@login_required
@user_passes_test(lambda u: u.is_staff)
def proveedor_create(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedor_list')
    else:
        form = ProveedorForm()
    return render(request, 'plantillas/proveedor_form.html', {'form': form})

# Vista para editar un proveedor existente
@login_required
@user_passes_test(lambda u: u.is_staff)
def proveedor_update(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedor_list')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'plantillas/proveedor_form.html', {'form': form})

# Vista para eliminar un proveedor
@login_required
@user_passes_test(lambda u: u.is_staff)
def proveedor_delete(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('proveedor_list')
    return render(request, 'plantillas/proveedor_confirm_delete.html', {'proveedor': proveedor})

###*************** FIN VISTAS CRUD PROVEEDORES ***************###

###################CRUD LOCALES ################################
# Vista para listar locales
@login_required
@user_passes_test(lambda u: u.is_staff)
def local_list(request):
    locales = Local.objects.all()
    return render(request, 'plantillas/local_list.html', {'locales': locales})

# Vista para crear un nuevo local
@login_required
@user_passes_test(lambda u: u.is_staff)
def local_create(request):
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('local_list')
    else:
        form = LocalForm()
    return render(request, 'plantillas/local_form.html', {'form': form})

# Vista para editar un local existente
@login_required
@user_passes_test(lambda u: u.is_staff)
def local_update(request, pk):
    local = get_object_or_404(Local, pk=pk)
    if request.method == 'POST':
        form = LocalForm(request.POST, instance=local)
        if form.is_valid():
            form.save()
            return redirect('local_list')
    else:
        form = LocalForm(instance=local)
    return render(request, 'plantillas/local_form.html', {'form': form})

# Vista para eliminar un local
@login_required
@user_passes_test(lambda u: u.is_staff)
def local_delete(request, pk):
    local = get_object_or_404(Local, pk=pk)
    if request.method == 'POST':
        local.delete()
        return redirect('local_list')
    return render(request, 'plantillas/local_confirm_delete.html', {'local': local})

###********************* FIN CRUD LOCALES *********************###

#pagina inicio
def inicio(request):
    return render(request, 'plantillas/inicio.html')

#pagina sobre nosotros :)
def sobre_nosotros(request):
    return render(request, 'plantillas/sobre_nosotros.html')

#carrito de compra
@login_required(login_url='login')
def agregar_al_carro(request, producto_id):
    producto = get_object_or_404(productos, id=producto_id)
    carrito = request.session.get('carrito', {})
    if producto_id not in carrito:
        carrito[producto_id] = {
            'nombre': producto.nombre,
            'precio': str(producto.precio),
            'cantidad': 1,
            'imagen': producto.imagen.url,
        }
    else:
        carrito[producto_id]['cantidad'] += 1

    request.session['checkout'] = checkout
    return redirect('checkout')  

#Funcion que dirige a edicion de productos "solo deben ingresar administradores"
@login_required
@user_passes_test(lambda u: u.is_staff)
def edit(request):
    edit = productos.objects.all()
    return render(request, 'edit/productos.html', {'edit': edit}) 
    
#vista del login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Has iniciado sesión como {username}.")
                return redirect(reverse('inicio'))
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    form = AuthenticationForm()
    return render(request=request, template_name="plantillas/login.html", context={"login_form": form})

#registro de usuarios
def registro_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso.")
            return redirect(reverse('inicio'))
        else:
            messages.error(request, "Registro no exitoso. Información inválida.")
    else:
        form = UserCreationForm()
    return render(request=request, template_name="plantillas/registro.html", context={"registro_form": form})


def logout_view(request):
    logout(request)
    return redirect(reverse('inicio'))


def lista_productos(request):
    productos_list = productos.objects.all()
    return render(request, 'plantillas/login.html', {'productos': productos_list})

def empezar(request):
    productos_list = productos.objects.all()
    return render(request, 'edit/lista_productoss.html', {'productos': productos_list})

def crear_producto(request):
    formulario = ProductosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('edit')
    return render(request, 'edit/crear.html', {'formulario': formulario})

def editar(request, id):
    producto = get_object_or_404(productos, id=id)
    formulario = ProductosForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('edit')
    return render(request, 'edit/editar.html', {'formulario': formulario})

def eliminar(request, id):
    producto = get_object_or_404(productos, id=id)
    producto.delete()
    return redirect('edit')

def tienda(request):
    carrito = Carrito(request).get_carrito()  # Usamos el método get_carrito aquí
    # Verificamos que todos los elementos tengan la clave 'precio_unitario'
    for item in carrito.values():
        if 'precio_unitario' not in item:
            item['precio_unitario'] = 0
    total = sum(item['precio_unitario'] * item['cantidad'] for item in carrito.values())  # Calcula el total
    return render(request, 'carro/tienda.html', {'carrito': carrito, 'total': total})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(productos, id=producto_id)
    carrito.agregar(producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    try:
        carrito = Carrito(request)
        producto = get_object_or_404(productos, id=producto_id)
        carrito.restar(producto)
    except productos.DoesNotExist:
        messages.error(request, "El producto no existe.")
    return redirect("tienda")

def sumar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(productos, id=producto_id)
    carrito.agregar(producto)
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    try:
        producto = get_object_or_404(productos, id=producto_id)
        carrito.eliminar(producto)
    except productos.DoesNotExist:
        messages.error(request, "El producto no existe.")
    return redirect("tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")

#pago seguro
def checkout(request):
    return render(request, 'carro/checkout.html')


