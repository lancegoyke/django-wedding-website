from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path, include


urlpatterns = [
    re_path(r'^', include('wedding.urls')),
    re_path(r'^', include('guests.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path('^accounts/', include('django.contrib.auth.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
