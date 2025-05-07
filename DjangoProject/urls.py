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
# """
# URL configuration for DjangoProject project.
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# # from django.contrib import admin
# from django.urls import path
#
# from DjangoProject.model_test.views import ModelTest, api
#
# urlpatterns = [
#     #    path('admin/', admin.site.urls),
#     path('model_test', ModelTest.as_view()),
#     path('api/', api.urls)
# ]
