from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path('nombre/<str:nombre>/<str:apellido>/', views.nombre),
]
