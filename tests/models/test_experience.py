from django.contrib.auth import get_user_model
from django.test import TestCase

from experience.models import Experience
from tests.factories import ResumeFactory, ExperienceFactory


class ExperienceTestCase(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_superuser(
            username="superuser",
            email="1@3.com",
            password="1234567890",
        )

        self.resume = ResumeFactory.build(owner=user)
        self.experience = ExperienceFactory.build(owner=user, resume=self.resume)

    def test_create_resume(self):
        self.assertIsNotNone(self.experience)

    def test_save_resume(self):
        self.resume.save()
        self.experience.save()
        item = Experience.objects.get(pk=self.experience.pk)
        self.assertIsNotNone(item)
