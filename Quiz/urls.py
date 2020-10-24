from django.urls import path, include
from Quiz.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('router-quiz', QuizViewSet)
router.register('router-question', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-quiz/', RegisterQuiz.as_view(), name='create-quiz'),
    path('quiz-display/', QuizDisplay.as_view(), name='quiz-display-all'),
    path('quiz-delete/<int:quiz_id>/', DeleteQuiz.as_view(), name='delete_quiz'),

    path('create-question/<int:quiz_id>/',
         RegisterQuestions.as_view(), name='create-question'),
    path('question-delete/<int:question_id>/',
         DeleteQuestion.as_view(), name='delete_question'),
    path('questions-display/<int:quiz_id>/',
         QuestionsDisplay.as_view(), name='questions-display-all'),

    path('update-question/<int:question_id>/',
         UpdateQuestion.as_view(), name='question-update'),
    path('update-quiz/<quiz_id>/', UpdateQuiz.as_view(), name='quiz-update'),

    path('take-quiz/<quiz_id>/', TakeQuiz.as_view(), name='take-quiz'),
    path('result/<quiz_id>/', Result.as_view(), name='result'),
]
