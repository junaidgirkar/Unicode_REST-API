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

from .api import UserAPIView,CreateUserView, RegisterAPIView, LoginAPIView, StudentRegisterAPIView, UserDisplayView, StudentDisplayView, TeacherDisplayView
from .api import TeacherRegisterAPIView, RegisterAPI1
from .api import *
urlpatterns = [
# WORKING STUFF:
    path('api/register/', RegisterAPI1.as_view(), name='register'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),




    path('', include('knox.urls')),
    path('users-display/', UserDisplayView.as_view()),
    path('students-display/', StudentDisplayView.as_view()),
    path('teachers-display/', TeacherDisplayView.as_view()),

    path('user/', UserAPIView.as_view()),
    #path('user-register/', views.create_auth),
    path('user-register/', CreateUserView.as_view()),
    path('student-register/', StudentRegisterAPIView.as_view()),
    path('teacher-register/', TeacherRegisterAPIView.as_view()),

    path('login1/', LoginAPIView.as_view()),
    path('logout1/', LogoutView.as_view(), name='knox_logout'),

    #"""     NEW STUFF       """


    #path('api/login/', LoginAPI.as_view(), name='login'),

]
