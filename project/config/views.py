from django.http import HttpResponse
from django.template import Template, Context

def test(request):
  html = open('./templates/template.html', encoding='utf-8')
  template = Template(html.read())
  html.close()
  context = Context({ "saludo": '¡Hola!' })
  document = template.render(context)
  return HttpResponse(document)