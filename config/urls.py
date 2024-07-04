from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("newsletters/", include("newsletters.urls", namespace="newsletters")),
    path("clients/", include("clients.urls", namespace="clients")),
    path("letters/", include("letters.urls", namespace="letters")),
]
