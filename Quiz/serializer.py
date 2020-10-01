from rest_framework import serializers
from Quiz.models import Quiz, Question

class QuizDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
        read_only_fields = ('__all__',)

class QuestionsDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ('__all__',)

class RegisterQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class RegisterQuizSerializer(serializers.ModelSerializer):


    def addQuestion(self, validated_data):

        quiz = Quiz.objects.create(
            question_text = validated_data['question_text'],
            option1 =validated_data['option1'],
            option2 =validated_data['option2'],
            option3 =validated_data['option3'],
            option4 =validated_data['option4'],
            correct_answer=validated_data['correct_answer'],
        )
        ordered_queryset = Question.objects.filter(question__id=obj.id).order_by('?')
        return RegisterQuestionSerializer(ordered_queryset, many=True, context=self.context).data

        quiz.save()

        return quiz

    class Meta:
        model = Quiz
        fields = '__all__'