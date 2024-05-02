from django.db import models

class User(models.Model):
  username = models.CharField(max_length=100)
  password = models.CharField(max_length=100)

  def __str__(self):
    return self.username

class Client(models.Model):
  name = models.CharField(max_length=100)
  surname = models.CharField(max_length=100)
  date = models.DateField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  email = models.EmailField()

  def __str__(self):
    return f"{self.surname}, {self.name}"
