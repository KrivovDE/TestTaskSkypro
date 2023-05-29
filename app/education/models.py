from uuid import uuid4

from behaviors.behaviors import Timestamped
from django.contrib.auth import get_user_model
from django.db import models


class Education(Timestamped):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=255, null=False, blank=False)
    start = models.DateField(null=False, blank=False)
    stop = models.DateField(null=False, blank=False)
    speciality = models.CharField(max_length=255, null=False, blank=False)
    profession = models.CharField(max_length=255, null=False, blank=False)
    resume = models.ForeignKey(
        "resume.Resume",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
    )
