from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('cliente/', include('cliente.urls')),
    path('producto/', include('producto.urls')),
]
