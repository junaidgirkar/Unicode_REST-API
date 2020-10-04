from django.shortcuts import render
from rest_framework import generics
from Quiz.models import Quiz, Question
from .serializer import QuizDisplaySerializer, RegisterQuizSerializer, RegisterQuestionSerializer, QuestionsDisplaySerializer
from knox.models import AuthToken
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import redirect
from django.db.models import Count
# Create your views here.

### This Signifies New Biginning ###


class RegisterQuestions(generics.GenericAPIView):
    serializer_class = RegisterQuestionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, quiz_id, *args, **kwargs):
        serializer = RegisterQuestionSerializer(data=request.data)
        instance = Quiz.objects.get(id=quiz_id)
        if Question.objects.filter(quiz=instance).aggregate(Count('question_text'))[
            'question_text__count'] > instance.total_questions:
            return Response({'response': "MAX QUESTIONS ADDED"})
        else:
            if serializer.is_valid():
                serializer.save(quiz=instance)
                question_count = Question.objects.filter(quiz=instance).aggregate(Count('question_text'))[
                            'question_text__count'] + 1
                if question_count <= instance.total_questions:
                    context = {
                        'response': 'Question successfully added',
                        'quiz id': quiz_id,
                    }

                else:
                    return redirect('questions-display-all', quiz_id)

                return Response(context)
            else:
                return Response(serializer.errors)


class QuestionsDisplay(generics.GenericAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, quiz_id, *args, **kwargs):
        specific_quiz = Quiz.objects.get(id=quiz_id)
        return Response(
            {
                'Questions': list(Question.objects.filter(quiz=specific_quiz).values())
            }
        )


class QuizDisplay(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.user.is_student:
            quizzes = list(Quiz.objects.all().values())
        else:
            quizzes = list(Quiz.objects.filter(teacher=request.user).values())
        context = {
            'quizzes': quizzes
        }
        return Response(context)


class DeleteQuiz(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,quiz_id, *args, **kwargs):
        try:

            Quiz.objects.get(id=quiz_id).delete()
            context = {
                "response" : "Quiz successfully deleted"
            }

        except:
            context = {
                "response" : "INVALID ID ENTERED !"
            }
        return Response(context)


class DeleteQuestion(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,question_id, *args, **kwargs):
        try:
            Question.objects.get(id=question_id).delete()
            response = {
                "response" : "Question successfully deleted"
            }
        except:
            response = {
                "response" : "INVALID ID ENTERED !"
            }
        return Response(response)


class RegisterQuiz(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RegisterQuizSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterQuizSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        quiz = serializer.save()
        """
        return Response({
        "quiz": RegisterQuizSerializer(quiz, context=self.get_serializer_context()).data,
        })
        """
        return redirect('create-question', quiz.id)


class UpdateQuestion(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RegisterQuestionSerializer

    def post(self, request, *args, **kwargs):
        question = Question.objects.get(id=kwargs['question_id'])
        serializer = RegisterQuestionSerializer(question,data=request.data)
        if serializer.is_valid():
            correct = serializer.validated_data['correct_answer']
            serializer.save(data=request.data)
            return Response({'response':'Question updated'})
        else:
            return Response(serializer.errors)


class UpdateQuiz(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RegisterQuizSerializer

    def post(self,request,quiz_id,*args,**kwargs):
        quiz = Quiz.objects.get(id=quiz_id)
        serializer = RegisterQuizSerializer(quiz,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'response':'Quiz Updated'})
        else:
            return Response(serializer.errors)