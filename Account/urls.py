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

from knox.views import LogoutView

from .api import UserAPIView, RegisterAPIView, LoginAPIView, StudentRegisterAPIView

urlpatterns = [
    path('', include('knox.urls')),
    path('user/', UserAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('student-register/', StudentRegisterAPIView.as_view()),
    path('login1/', LoginAPIView.as_view()),
    path('logout1/', LogoutView.as_view(), name='knox_logout')

]
