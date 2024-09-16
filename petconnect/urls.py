from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('animal/', include('animal.urls')),
    path('adocao/', include('adocao.urls')),
    path('adotante/', include('adotante.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
