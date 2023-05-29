from datetime import datetime

from factory.django import DjangoModelFactory


class EducationFactory(DjangoModelFactory):
    class Meta:
        model = "education.Education"
        django_get_or_create = ("name", "resume")

    name = "test - name"
    start = datetime.now()
    stop = datetime.now()
