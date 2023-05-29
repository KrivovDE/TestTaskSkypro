from django.db.models import QuerySet

from rest_framework.mixins import UpdateModelMixin

from rest_framework.viewsets import GenericViewSet

from .serializers import ExperienceSerializer, Experience


class ExperienceViewSet(
    UpdateModelMixin,
    GenericViewSet,
):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()
    http_method_names = [
        "patch",
    ]

    def get_queryset(self) -> QuerySet[Experience]:
        return super().get_queryset().filter(owner=self.request.user)
