from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.TaskListCreateView.as_view()),
    path('<int:id>/', views.TaskRetriveUpdateDestroyView.as_view(), name='task-detail'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]