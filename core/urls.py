from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('home.urls')),
    path('catalog/', include('category.urls')),
]

if settings.DEBUG:
    # do not do this in production
    from django.conf.urls.static import static

    # try django
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)