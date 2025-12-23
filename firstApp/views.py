from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    return HttpResponse ("<h1>Welcome to the Task Management Application!</h1>")

def task_list(request):
    tasks= Task.objects.all()
    return render(request,'firstApp/task_list.html',{'tasks':tasks})

class TaskListView(ListView):
    model=Task #select * from task  
    template_name="firstApp/task_list.html"
    context_object_name="tasks" #le nom est au choix #l'objet par défaut est object_list default # on ajoute cette ligne sinon on va afficher rien , on dirait on va lier à notre modèle Task
    def get_queryset(self):     #cette fonction à utiliser pour ajouter un filtre pour notre requête
        #return Task.objects.all().order_by('due_date)
        return Task.objects.exclude(status='DONE')
    
    
    
class TaskDetailView(DetailView):
  model = Task
  template_name = 'firstApp/task_detail.html'
  context_object_name = 'task'


class TasKCreateView(CreateView):
    model= Task
    template_name="firstApp/task_form.html"
    #fields=['title','description','due_date','status']
    fields="__all__" #il va afficher tous les champs sans précision
    success_url=reverse_lazy('task_list')

class TasKUpdateView(UpdateView):
    model= Task
    template_name="firstApp/task_form.html"
    #fields=['title','description','due_date','status']
    fields="__all__" #il va afficher tous les champs sans précision
    success_url=reverse_lazy('task_list')
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'firstApp/task_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')   