from rest_framework import serializers

from api.v1.education import EducationSerializer
from api.v1.experience import ExperienceSerializer
from resume.models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    salary = serializers.SerializerMethodField(read_only=True)
    salary_from = serializers.IntegerField(write_only=True)
    salary_to = serializers.IntegerField(write_only=True)
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)
    education = serializers.SerializerMethodField(read_only=True)
    experience = serializers.SerializerMethodField(read_only=True)

    def get_education(self, obj) -> EducationSerializer:
        return EducationSerializer(obj.education_set.all(), many=True).data

    def get_experience(self, obj) -> ExperienceSerializer:
        return ExperienceSerializer(obj.experience_set.all(), many=True).data

    def get_salary(self, obj) -> str:
        return obj.salary

    class Meta:
        model = Resume
        fields = [
            "uid",
            "created",
            "modified",
            "status",
            "grade",
            "specialty",
            "portfolio",
            "title",
            "phone",
            "email",
            "salary",
            "owner",
            "salary_from",
            "salary_to",
            "education",
            "experience",
        ]
