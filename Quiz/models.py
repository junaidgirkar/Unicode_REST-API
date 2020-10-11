from django.db import models
from Account.models import Student, Teacher

# Create your models here.


class Quiz(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    total_questions = models.SmallIntegerField()

    def __str__(self):
        return self.subject + "_ID:" + str(self.id)

    class Meta:
        verbose_name_plural = 'Quizzes'


class Question(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255, default='Option1')
    option2 = models.CharField(max_length=255, default='Option2')
    option3 = models.CharField(max_length=255, default='Option3')
    option4 = models.CharField(max_length=255, default='Option4')
    correct_answer = models.CharField(max_length=255, default='CorrectAnswer')

    def __str__(self):
        return str(self.id)


class Answer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.student.email + "." + str(self.question.id)+"." + str(self.id)


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    score = models.SmallIntegerField()

    def __str__(self):
        return self.student.email + "." + self.quiz.subject
