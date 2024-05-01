from django.http import HttpResponse

def test(request):
  return HttpResponse('<p style="color: red; font-size: 24px;">Hello, World!</p>')

def nombre(request, nombre: str, apellido: str):
  nombre = nombre.capitalize()
  apellido = apellido.capitalize()
  return HttpResponse(f'<p style="color: red; font-size: 24px;">{nombre} {apellido}</p>')