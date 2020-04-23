from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
	tasks=Task.objects.all()
	form=TaskForm()
	if request.method=="POST":
		form=TaskForm(request.POST)
		if form.is_valid():
			form.save()
			print('job done')
		return redirect('/')

	context={'tasks':tasks, 'form':form}

	return render(request, "tasks/index.html", context)


def UpdateTask(request, pk):
	tasks=Task.objects.get(id=pk)
	form=TaskForm(instance=tasks)
	if request.method=="POST":
		form=TaskForm(request.POST, instance=tasks)
		if form.is_valid():
			form.save()
		return redirect('/')
	context={'form':form}
	return render (request, "tasks/update_task.html", context)


def DeleteTask(request, pk):
	tasks=Task.objects.get(id=pk)

	if request.method=="POST":
		tasks.delete()
		return redirect('/')

	context={'tasks':tasks}

	return render(request, "tasks/delete_task.html", context)