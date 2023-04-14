from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tickets/', include('tickets.urls')),
    path('', include('tickets.urls')),  # Adicione esta linha
]