from django.shortcuts import render
from rest_framework import generics
from Quiz.models import Quiz, Question
from .serializer import QuizDisplaySerializer, RegisterQuizSerializer, RegisterQuestionSerializer, QuestionsDisplaySerializer
from knox.models import AuthToken
from rest_framework.response import Response

# Create your views here.


class QuizDisplay(generics.ListAPIView):
    serializer_class = QuizDisplaySerializer
    queryset = Quiz.objects.all()


class RegisterQuiz(generics.GenericAPIView):
    serializer_class = RegisterQuizSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        quiz = serializer.save()
        return Response({
        "quiz": RegisterQuizSerializer(quiz, context=self.get_serializer_context()).data,
        #"token": AuthToken.objects.create(user)[1]
        })

class RegisterQuestions(generics.GenericAPIView):
    serializer_class = RegisterQuestionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = serializer.save()
        return Response(
            {
                'question': RegisterQuestionSerializer(question, context=self.get_serializer_context()).data,
            }
        )

class QuestionsDisplay(generics.ListAPIView):
    serializer_class = QuestionsDisplaySerializer
    def get(self, request, quiz_id, *args, **kwargs):
        queryset = Question.objects.filter(quiz_id=quiz_id).order_by('?')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        questions = serializer.save()
        return Response(
            {
                "Questions": QuestionsDisplaySerializer(questions, context=self.get_serializer_context()).data,
            }
        )
