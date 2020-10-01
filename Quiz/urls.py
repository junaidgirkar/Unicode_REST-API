from django.urls import path, include
from Quiz.views import *

urlpatterns = [
    path('quiz-display/', QuizDisplay.as_view(), name='quiz-display-all'),
    path('create-quiz/', RegisterQuiz.as_view(), name='create-quiz'),
    path('create-question/', RegisterQuestions.as_view(), name='create-question'),
    path('questions-display/<int:quiz_id>/', QuestionsDisplay.as_view(), name='questions-display-all'),
]