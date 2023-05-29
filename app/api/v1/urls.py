from django.conf import settings
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter, SimpleRouter

from .education import EducationViewSet
from .experience import ExperienceViewSet
from .resume import ResumeViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("resume", ResumeViewSet)
router.register("education", EducationViewSet)
router.register("experience", ExperienceViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/schema/", SpectacularAPIView.as_view(), name="api-schema_v1"),
    path(
        "v1/docs/",
        SpectacularSwaggerView.as_view(url_name="api:api-schema_v1"),
        name="api-docs_v1",
    ),
]
