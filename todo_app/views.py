from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at') # Added ordering so new tasks appear at top
    
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('task_image') # Get the image from the request
        
        if title:
            # CORRECTED: Added 'image=image' so the photo actually saves to the database
            Task.objects.create(title=title, image=image) 
        
        return redirect('task_list') # Redirect using the name of the URL
    
    return render(request, 'todo_app/todo.html', {'tasks': tasks})

def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk) # Using get_object_or_404 is safer
    task.delete()
    return redirect('task_list')

def complete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')