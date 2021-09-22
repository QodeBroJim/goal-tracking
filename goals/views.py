from django.shortcuts import (  get_object_or_404, redirect, 
                                render, reverse)

from .forms import CategoryForm, GoalForm, TaskForm
from .models import Category, Goal, Task

""" Category Related Views """
# display the user's categories
def categories_list(request):
    categories = Category.objects.filter(author=request.user).order_by('title')
    context = {
        'categories': categories,
    }
    return render(request, 'goals/categories/categories.html', context)

# single category
def single_category(request, pk):
    category = get_object_or_404(Category, url=pk)

    form = CategoryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.category = category
            form.save()
            return redirect(reverse('category-detail', kwargs={
                'pk': pk
            }))
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'goals/categories/single_category.html', context)

# create a goal category
def category_create(request):
    title = 'Create'
    instance = Category(author=request.user)
    form = CategoryForm(instance=instance)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect(reverse('category-detail', kwargs={
                'pk': form.instance.url
            }))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'goals/categories/category_create_form.html', context)

# update a category
def category_update(request, pk):
    title = 'Update'
    category = get_object_or_404(Category, url=pk)
    form = CategoryForm(request.POST or None, request.FILES or None, instance=category)
    author = request.user
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('category-detail', kwargs={
                'pk': form.instance.url
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, 'goals/categories/category_create_form.html', context)

# delete a category
def category_delete(request, pk):
    category = get_object_or_404(Category, url=pk)
    category.delete()
    return redirect(reverse('category-list'))

""" Goal Related Views """
# display the user's goals
def goal_dashboard(request):
    goals = Goal.objects.filter(author=request.user).order_by('category', 'id')
    context = {
        'goals': goals,
    }
    return render(request, 'goals/goal_dashboard.html', context)

# single goal
def single_goal(request, pk):
    goal = get_object_or_404(Goal, url=pk)

    form = GoalForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.goal = goal
            form.save()
            return redirect(reverse('goal-detail', kwargs={
                'pk': pk
            }))
    context = {
        'form': form,
        'goal': goal,
    }
    return render(request, 'goals/single_goal.html', context)

# create a goal
def goal_create(request):
    title = 'Create'
    instance = Goal(author=request.user)
    form = GoalForm(instance=instance)
    
    if request.method == 'POST':
        form = GoalForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect(reverse('goal-detail', kwargs={
                'pk': form.instance.url
            }))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'goals/goal_create_form.html', context)

# update a goal
def goal_update(request, pk):
    title = 'Update'
    goal = get_object_or_404(Goal, url=pk)
    form = GoalForm(request.POST or None, request.FILES or None, instance=goal)
    author = request.user
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('goal-detail', kwargs={
                'pk': form.instance.url
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, 'goals/goal_create_form.html', context)

# delete a category
def goal_delete(request, pk):
    goal = get_object_or_404(Category, url=pk)
    goal.delete()
    return redirect(reverse('goal-dashboard'))

""" Task Related Views """
# display the goal's tasks
def task_list(request):
    tasks = Task.objects.filter(author=request.user, goal='goal__goal').order_by('id', 'goal__goal')
    context = {
        'tasks': tasks,
    }
    return render(request, 'goals/tasks/task_list.html', context)

# single task
def single_task(request, pk):
    task = get_object_or_404(Task, url=pk)

    form = TaskForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.task = task
            form.save()
            return redirect(reverse('task-detail', kwargs={
                'pk': pk
            }))
    context = {
        'form': form,
        'task': task,
    }
    return render(request, 'goals/tasks/single_task.html', context)

# create a task
def task_create(request):
    title = 'Create'
    instance = Task(author=request.user)
    form = TaskForm(instance=instance)
    
    if request.method == 'POST':
        form = TaskForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect(reverse('task-detail', kwargs={
                'pk': form.instance.url
            }))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'goals/tasks/task_create_form.html', context)

# update a task
def task_update(request, pk):
    title = 'Update'
    task = get_object_or_404(Task, url=pk)
    form = TaskForm(request.POST or None, request.FILES or None, instance=task)
    author = request.user
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('task-detail', kwargs={
                'pk': form.instance.url
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, 'goals/tasks/task_create_form.html', context)

# delete a category
def task_delete(request, pk):
    task = get_object_or_404(Task, url=pk)
    task.delete()
    return redirect(reverse('task-list'))
