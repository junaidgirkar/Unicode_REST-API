from django.contrib import admin
from Quiz.models import *
# Register your models here.

class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher', 'subject', 'total_questions']
    search_fields = ['id']
    filter_horizontal =()
    list_filter = ()
    fieldsets = ()
    ordering = ['id']


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Result)