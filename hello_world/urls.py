from django.contrib import admin
from django.urls import path, include

from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter


urlpatterns = [
    
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/schema/', SpectacularAPIView.as_view(),name="schema"),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name="schema")),
    path("", include('app.urls'))
    
    ]
