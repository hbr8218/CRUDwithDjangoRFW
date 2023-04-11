from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

from .models import Task
from .serializers import TaskSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class TaskListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    # def get_queryset(self):
    #     return self.queryset.filter(owner = self.request.user)


class TaskRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'





class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer