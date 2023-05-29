from factory.django import DjangoModelFactory


class ResumeFactory(DjangoModelFactory):
    class Meta:
        model = "resume.Resume"
        django_get_or_create = ("owner",)
