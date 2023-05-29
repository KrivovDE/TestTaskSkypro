from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tests.factories import ResumeFactory, EducationFactory, ExperienceFactory
from rest_framework.test import APIClient


class EducationApiTestCase(TestCase):
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

    def test_path(self):
        url = reverse("api:education-detail", args=[self.education.pk])
        self.client.force_authenticate(self.user)
        response = self.client.patch(url, data={"name": "change name"}).json()
        self.assertEqual("change name", response["name"])

    def test_path_another_user(self):
        url = reverse("api:education-detail", args=[self.education.pk])
        user = get_user_model().objects.create_superuser(
            username="another_user",
            email="2@3.com",
            password="1234567890",
        )
        self.client.force_authenticate(user)
        response = self.client.patch(url, data={"name": "change name"}).json()
        self.assertEqual({"detail": "Страница не найдена."}, response)
