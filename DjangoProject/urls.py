# urls.py
from django.urls import re_path, path
from rest_framework.routers import DefaultRouter
from .casmal_test.views import ExperimentViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'experiments', ExperimentViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="ML API",
      default_version='v1',
      description="Experiment management API",
   ),
   public=True,
)

urlpatterns = [
    *router.urls,
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]
