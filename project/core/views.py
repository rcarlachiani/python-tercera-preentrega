from django.shortcuts import render
from producto import models

def home(request):
  return render(request, 'core/index.html')