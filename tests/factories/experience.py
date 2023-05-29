from datetime import datetime

from factory.django import DjangoModelFactory


class ExperienceFactory(DjangoModelFactory):
    class Meta:
        model = "experience.Experience"
        django_get_or_create = ("employer", "owner", "resume")

    employer = "employer - test"
    start = datetime.now()
    stop = datetime.now()
