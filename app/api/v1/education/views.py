from django.db.models import QuerySet

from rest_framework.mixins import UpdateModelMixin

from rest_framework.viewsets import GenericViewSet

from .serializers import EducationSerializer, Education


class EducationViewSet(
    UpdateModelMixin,
    GenericViewSet,
):
    serializer_class = EducationSerializer
    queryset = Education.objects.all()
    http_method_names = [
        "patch",
    ]

    def get_queryset(self) -> QuerySet[Education]:
        return super().get_queryset().filter(owner=self.request.user)
