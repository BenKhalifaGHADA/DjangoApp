from django.contrib import admin
from django.urls import path
from .views import home,task_list,TaskListView,TaskDetailView,TasKCreateView,TasKUpdateView,TaskDeleteView
urlpatterns = [
    path('', home, name='firstApp_home'),
    path('tasks/',task_list, name='task_list'),
    path('tasks-class/',TaskListView.as_view(),name='task_list_class'),
    #Exemple des routes paramétrés 
    path('tasks/<int:pk>/',TaskDetailView.as_view(), name='taskdetail'),

    path('tasks/create/',TasKCreateView.as_view(), name='taskcreate'),
    path('tasks/update/<int:pk>/',TasKUpdateView.as_view(), name='taskupdate'),
    path('tasks/delete/<int:pk>/',TaskDeleteView.as_view(), name='taskdelete'),
]
