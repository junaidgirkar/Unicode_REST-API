from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from knox.models import AuthToken
from .models import *
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer,UserRegisterSerializer ,RegisterSerializer, LoginSerializer, StudentRegisterSerializer, StudentSerializer, StudentDisplaySerializer, TeacherDisplaySerializer
from .serializers import TeacherRegisterSerializer, RegisterSerializer1
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserRegisterSerializer




class UserDisplayView(APIView):
    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(User.objects.all(), pk=pk)
            serializer = UserSerializer(user)
            return Response({"user": serializer.data})
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})


class StudentDisplayView(APIView):
    def get(self, request, pk=None):
        if pk:
            student = get_object_or_404(Student.objects.all(), pk=pk)
            serializer = StudentDisplaySerializer(student)
            return Response({"student": serializer.data})
        students = Student.objects.all()
        serializer = UserSerializer(students, many=True)
        return Response({"students": serializer.data})


class TeacherDisplayView(APIView):
    def get(self, request, pk=None):
        if pk:
            teacher = get_object_or_404(Teacher.objects.all(), pk=pk)
            serializer = TeacherDisplaySerializer(teacher)
            return Response({"teacher": serializer.data})
        teachers = Teacher.objects.all()
        serializer = UserSerializer(teachers, many=True)
        return Response({"teachers": serializer.data})




class UserAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def get(self, request):
        return self.request.user


class RegisterAPIView(generics.CreateAPIView):

    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )
    queryset = User.objects.all()

 #def post(self, request, *args, **kwargs):
 #       serializer = self.get_serializer(data=request.data)
  #      serializer.is_valid(raise_exception=True)
   #     user = serializer.save()
   #     return Response({
   #         "user": UserSerializer(user, context=self.get_serializer_context()).data,
   #         "token": AuthToken.objects.create(user)[1]
   #     })


class StudentRegisterAPIView(generics.GenericAPIView):
    '''model = Student
    permission_classes = [
        permissions.AllowAny# Or anon users can't register
    ]
    serializer_class = StudentRegisterSerializer'''

    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head']
    def get(self, request, format=None):
        users = Student.objects.all()
        serializer = StudentRegisterSerializer(users, many=True)
        return Response(serializer.data)


class TeacherRegisterAPIView(generics.GenericAPIView):
    model = Teacher
    permission_classes = [
        permissions.AllowAny# Or anon users can't register
    ]
    serializer_class = TeacherRegisterSerializer



class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response({
            'user': UserSerializer(user).data,
            'token': AuthToken.objects.create(user)[1]
        })
"""         NEW STUFF           """





class RegisterAPI1(generics.GenericAPIView):
    serializer_class = RegisterSerializer1

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)