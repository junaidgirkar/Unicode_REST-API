"""Unicode_REST_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from knox import views as knox_views
from knox.views import LogoutView
from Account.views import welcomePage
from .api import *
urlpatterns = [
# WORKING STUFF:
    path('user-register/', RegisterUser.as_view(), name='user-register'),
    path('student-register/', RegisterStudent.as_view(), name='student-register'),
    path('teacher-register/', RegisterTeacher.as_view(), name='teacher-register'),

    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),


    path('users-display/', UserDisplayView.as_view(), name='user-display-all'),
    path('users-display/<int:pk>/', UserDisplayView.as_view(), name='user-display-single'),

    path('students-display/', StudentDisplayView.as_view(), name='student-display-all'),
    path('students-display/<int:pk>/', UserDisplayView.as_view(), name='student-display-single'),

    path('teachers-display/', TeacherDisplayView.as_view(), name='teacher-display-all'),
    path('teachers-display/<int:pk>/', UserDisplayView.as_view(), name='teacher-display-single'),


    path('', welcomePage),
    path('user/', UserAPIView.as_view()),


   # path('logout1/', LogoutView.as_view(), name='knox_logout'),


]
