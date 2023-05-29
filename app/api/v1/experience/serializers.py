from rest_framework import serializers

from experience.models import Experience


class ExperienceSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    resume = serializers.UUIDField(write_only=True)

    class Meta:
        model = Experience
        fields = [
            "pk",
            "owner",
            "employer",
            "desc",
            "start",
            "stop",
            "is_this_monente",
            "resume",
        ]
