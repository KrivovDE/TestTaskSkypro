from rest_framework import serializers

from education.models import Education


class EducationSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    resume = serializers.UUIDField(write_only=True)

    class Meta:
        model = Education
        fields = [
            "pk",
            "name",
            "start",
            "stop",
            "speciality",
            "profession",
            "owner",
            "resume",
        ]
