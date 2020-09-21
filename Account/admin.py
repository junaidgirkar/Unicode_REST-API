from django.contrib import admin
from .models import Student, User, Teacher
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class BaseUserAdmin(UserAdmin):
    list_display = ['email', 'is_admin', 'is_student', 'is_teacher']
    search_fields = ()
    filter_horizontal =()
    list_filter = ()
    fieldsets = ()
    ordering = ['email']

class StudentAdmin(UserAdmin):
    list_display = ['email', 'is_admin', 'is_student', 'is_teacher']
    search_fields = ()
    filter_horizontal =()
    list_filter = ()
    fieldsets = ()
    ordering = ['email']

class TeacherAdmin(UserAdmin):
    list_display = ['email', 'is_admin', 'is_student', 'is_teacher']
    search_fields = ()
    filter_horizontal =()
    list_filter = ()
    fieldsets = ()
    ordering = ['email']


admin.site.unregister(Group)
admin.site.register(User, BaseUserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)