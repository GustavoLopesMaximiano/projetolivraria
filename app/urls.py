from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet, EditoraViewSet, UserViewSet, AutorViewSet

router = DefaultRouter()

router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'editoras', EditoraViewSet)
router.register(r'autores', AutorViewSet)

urlpatterns = [
    path('', lambda request: redirect('/api/swagger/')),

    path('admin/', admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),

    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),

    path('api/', include(router.urls)),
]