from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from tercera_prentrega_cuello import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplicacion.urls')),
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
