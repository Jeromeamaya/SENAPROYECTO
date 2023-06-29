from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prodev/', include('prodev.urls')),
    path('', include('prodev.urls')),  # Agrega esta línea
]
