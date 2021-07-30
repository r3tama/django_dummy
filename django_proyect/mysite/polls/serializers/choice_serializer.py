from rest_framework import serializers
from polls.models import Choice
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "choice_text",
            "votes",
            "id",
        ]
        model = Choice
