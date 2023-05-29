from django.contrib.auth import get_user_model
from django.test import TestCase

from resume.models import Resume
from tests.factories import ResumeFactory


class ResumeTestCase(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_superuser(
            username="superuser",
            email="1@3.com",
            password="1234567890",
        )

        self.resume = ResumeFactory.build(owner=user)

    def test_create_resume(self):
        self.assertIsNotNone(self.resume)

    def test_salary_resume(self):
        self.assertEqual(
            self.resume.salary,
            f"{self.resume.salary_from} - {self.resume.salary_to}",
        )

    def test_save_resume(self):
        self.resume.save()
        resume = Resume.objects.get(pk=self.resume.pk)
        self.assertIsNotNone(resume)
