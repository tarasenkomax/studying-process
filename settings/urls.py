from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from settings.settings import DEBUG

schema_view = get_schema_view(
    openapi.Info(
        title="METASHARKS. ©tarasenkomax",
        default_version='v1',
        description="Тестовое задание для компании METASHARKS",
        contact=openapi.Contact(url="https://t.me/tarasenko_m"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("studying_process.urls")),
    path('api-auth/', include('rest_framework.urls')),
]
if DEBUG:
    urlpatterns += [
        path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
        path('__debug__/', include('debug_toolbar.urls')),
    ]
