from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from ninja import NinjaAPI

from main.api.v1.router import router as main_router

api_v1 = NinjaAPI()
api_v1.add_router("main", main_router, tags=["Main"])

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", api_v1.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
