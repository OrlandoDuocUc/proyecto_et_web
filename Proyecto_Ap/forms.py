from django import forms
from .models import productos, Proveedor, Local
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductosForm(forms.ModelForm):
    class Meta:
        model = productos
        fields ='__all__'

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        
        
#creamos un nuevo formulario para manejar en este caso los proveedores
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono', 'email', 'descripcion']     
        
#creamos el formulario para manejar los locales.        
class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nombre', 'direccion', 'telefono', 'email', 'horario']        
           