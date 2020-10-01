from django.contrib import admin
from Quiz.models import *
# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Result)