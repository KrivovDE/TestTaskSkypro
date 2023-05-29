from django.contrib import admin

from education.models import Education
from experience.models import Experience
from .models import Resume


class EducationTabularInline(admin.TabularInline):
    model = Education
    extra = 0
    exclude = [
        "created",
        "modified",
        "owner",
    ]


class ExperienceTabularInline(admin.TabularInline):
    model = Experience
    extra = 0
    exclude = [
        "created",
        "modified",
        "owner",
    ]


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    inlines = [EducationTabularInline, ExperienceTabularInline]
