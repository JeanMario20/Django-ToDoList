from django.shortcuts import render
from django.shortcuts import redirect
from .forms import formTaks
from .models import task

# Create your views here.

def list(request):
    allTask = task.objects.all()
    context = {'allTask': allTask}

    return render (request, "table.html",context)

def add_taks(request):
    form = formTaks
    if request.method == 'POST':
        form = formTaks(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {'form':form}
    return render(request, 'add_task.html', context)

def editTask(request, pk):
    task_id = task.objects.get(id=pk)
    form = formTaks(instance=task_id)

    if request.method =='POST':
        form = formTaks(request.POST, instance=task_id)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {'form':form}
    return render(request, 'add_task.html', context)

def deleteTask(request, pk):
    task_data = task.objects.get(id=pk)
    task_data.delete()
    return redirect(list)