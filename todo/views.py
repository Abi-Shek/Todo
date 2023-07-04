from django.shortcuts import render, redirect
from django.http.response import HttpResponse
# Create your views here.
from todo.models import Task


def home(request):
    task=Task.objects.filter(is_compeleted=False).order_by('-updated_ad')
    context={
        'tasks':task
    }
    return render(request,'home.html',context)
def addTask(request):
   task=request.POST['task']
   Task.objects.create(task=task)
   return redirect('home')