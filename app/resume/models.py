from uuid import uuid4

from behaviors.behaviors import Timestamped
from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .constants import StatusResume, GradeResume


class Resume(Timestamped):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    status = models.CharField(
        max_length=20,
        choices=StatusResume.choices,
        default=StatusResume.ACTIVE,
    )
    grade = models.CharField(
        max_length=20,
        choices=GradeResume.choices,
        default=GradeResume.JUNIOR,
    )
    specialty = models.CharField(max_length=255, null=True, blank=True)
    salary_from = models.IntegerField(null=True, blank=True)
    salary_to = models.IntegerField(null=True, blank=True)

    @property
    def salary(self):
        return f"{self.salary_from} - {self.salary_to}"

    portfolio = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=255)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
    )
