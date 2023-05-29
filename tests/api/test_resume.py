from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tests.factories import ResumeFactory, EducationFactory, ExperienceFactory
from rest_framework.test import APIClient


class ResumeApiTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username="superuser",
            email="1@3.com",
            password="1234567890",
        )
        self.resume = ResumeFactory.create(owner=self.user)
        self.education = EducationFactory.create(resume=self.resume, owner=self.user)
        self.experience = ExperienceFactory.create(resume=self.resume, owner=self.user)
        self.client = APIClient()

    def test_get(self):
        url = reverse("api:resume-list")
        self.client.force_authenticate(self.user)
        response = self.client.get(url).json()
        self.assertEqual(str(self.resume.pk), response[0]["uid"])
        self.assertIsNotNone(response[0]["education"])
        self.assertIsNotNone(response[0]["experience"])

    def test_get_another_user(self):
        url = reverse("api:resume-list")
        user = get_user_model().objects.create_superuser(
            username="another_user",
            email="2@3.com",
            password="1234567890",
        )
        self.client.force_authenticate(user)
        response = self.client.get(url).json()
        self.assertEqual([], response)

    def test_path(self):
        url = reverse("api:resume-detail", args=[self.resume.pk])

        self.client.force_authenticate(self.user)
        data = {
            "grade": "midle",
            "specialty": "test spect",
            "portfolio": "https://example.com",
            "title": "test title",
        }
        response = self.client.patch(url, data=data).json()
        for k, v in data.items():
            self.assertEqual(v, response[k])
