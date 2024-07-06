from django.db import models
from django.contrib.auth.models import User

class productos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100,verbose_name="Titulo")
    imagen = models.ImageField(upload_to='image/',verbose_name="Imagen", null=True, blank=True)
    descripcion = models.TextField(verbose_name="Descripcion",null=True)
    precio = models.IntegerField(verbose_name="Precio", default=1000)
        
    #categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)-->
    def __str__(self):
        fila= "TITULO: "+ self.titulo+ "  --  " + "DESCRIPCION: " + self.descripcion
        return fila
    
    def delete(self,using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        

#creamos nuevo modelo para nuevo crud para administrar los proveedores
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

#modelo nuevo para Locales
class Local(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    horario = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre



        