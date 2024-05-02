from django.db import models

class Categorias(models.Model):
  name = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.name
  
class Formatos(models.Model):
  name = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.name
  
class Producto(models.Model):
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  category = models.ForeignKey(Categorias, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.name} - {self.category} - U$S{self.price}"