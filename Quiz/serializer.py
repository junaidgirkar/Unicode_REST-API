from rest_framework import serializers
from Quiz.models import Quiz, Question, Answer


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


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
        fields = ['question_text', 'option1', 'option2',
                  'option3', 'option4', 'correct_answer']


class RegisterQuizSerializer(serializers.ModelSerializer):

    """def addQuestion(self, validated_data):

        quiz = Quiz.objects.create(
            question_text=validated_data['question_text'],
            option1=validated_data['option1'],
            option2=validated_data['option2'],
            option3=validated_data['option3'],
            option4=validated_data['option4'],
            correct_answer=validated_data['correct_answer'],
        )
        ordered_queryset = Question.objects.filter(
            question__id=obj.id).order_by('?')
        return RegisterQuestionSerializer(ordered_queryset, many=True, context=self.context).data

        quiz.save()

        return quiz
    """

    def __init__(self, *args, **kwargs):
        super(RegisterQuizSerializer, self).__init__(*args, **kwargs)
        teacher = self.context['request'].user

    class Meta:
        model = Quiz
        fields = ['subject', 'total_questions', 'teacher']


class TakeQuizSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(TakeQuizSerializer, self).__init__(many=many, *args, **kwargs)

    question = serializers.IntegerField()

    class Meta:
        model = Answer
        fields = ['question', 'answer']
