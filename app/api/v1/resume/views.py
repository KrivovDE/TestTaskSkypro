from django.db.models import QuerySet

from rest_framework.mixins import ListModelMixin, UpdateModelMixin

from rest_framework.viewsets import GenericViewSet

from .serializers import ResumeSerializer, Resume


class ResumeViewSet(
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()
    http_method_names = [
        "get",
        "patch",
    ]

    def get_queryset(self) -> QuerySet[Resume]:
        return super().get_queryset().filter(owner=self.request.user)
