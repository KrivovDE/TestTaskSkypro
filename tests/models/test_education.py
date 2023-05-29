from django.contrib.auth import get_user_model
from django.test import TestCase

from education.models import Education
from tests.factories import ResumeFactory, EducationFactory


class EducationTestCase(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_superuser(
            username="superuser",
            email="1@3.com",
            password="1234567890",
        )

        self.resume = ResumeFactory.build(owner=user)
        self.education = EducationFactory.build(resume=self.resume, owner=user)

    def test_create_resume(self):
        self.assertIsNotNone(self.resume)

    def test_save_resume(self):
        self.resume.save()
        self.education.save()
        item = Education.objects.get(pk=self.education.pk)
        self.assertIsNotNone(item)
