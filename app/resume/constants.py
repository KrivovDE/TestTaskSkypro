from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusResume(models.TextChoices):
    ACTIVE = "active", _("Active")
    UNACTIVE = "un_active", _("unActive")


class GradeResume(models.TextChoices):
    JUNIOR = "junior", _("Junior")
    MIDLE = "midle", _("Midle")
    SENIOR = "senior", _("Senior")
