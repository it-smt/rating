from django.contrib import admin
from django.urls import path

from ninja import NinjaAPI

from main.api.v1.router import router as main_router

api_v1 = NinjaAPI()
api_v1.add_router("main", main_router, tags=["Main"])

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", api_v1.urls),
]
