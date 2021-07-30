from rest_framework import serializers
from polls.models import Question

from polls.serializers.choice_serializer import ChoiceSerializer
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Question
    
    def to_representation(self, instance): 
        data = super(serializers.ModelSerializer, self).to_representation(instance)
        result = dict(data)
        result["choices"] = ChoiceSerializer(instance.question_choices, many=True).data
        return result
