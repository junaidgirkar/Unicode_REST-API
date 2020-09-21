from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager, StudentManager, TeacherManager
# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique = True)
    first_name = models.CharField(_('first_name'), max_length = 40)
    last_name = models.CharField(_('last name'), max_length = 40)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add = True)
    is_active = models.BooleanField(_('active'), default = True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_superuser = models.BooleanField(_('is superuser'), default = False)
    is_admin = models.BooleanField(_('is_admin'), default=False)
    is_student = models.BooleanField(_('is student'), default = False)
    is_teacher = models.BooleanField(_('is teacher'), default = False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_short_name(self):
        return self.first_name
    def get_full_name(self):\
        return self.first_name + "_" + self.last_name
    def save(self, *args, **kwargs):
        self.username = self.email
        super(User, self).save(*args, **kwargs)
    def __str__(self):
        return self.email

class Student(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)
    user.is_student = True
    user.is_teacher = False
    branch = models.CharField(max_length=40)

    objects = StudentManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.user.email

class Teacher(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)
    user.is_student=False
    user.is_teacher = True
    subject = models.CharField(max_length=40)
    objects = TeacherManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.user.email