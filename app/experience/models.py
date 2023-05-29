from uuid import uuid4

from behaviors.behaviors import Timestamped
from django.contrib.auth import get_user_model
from django.db import models


class Experience(Timestamped):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    employer = models.CharField(max_length=255, null=False, blank=False)
    desc = models.TextField(null=False, blank=False)
    start = models.DateField(null=False, blank=False)
    stop = models.DateField(null=False, blank=False)
    resume = models.ForeignKey(
        "resume.Resume",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    is_this_monente = models.BooleanField(null=False, blank=False, default=False)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
    )
