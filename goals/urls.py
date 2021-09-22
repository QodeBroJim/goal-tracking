from django.urls import path

from .views import (categories_list, category_create, category_delete,
                    category_update, single_category, single_goal, 
                    goal_dashboard, goal_delete, goal_update, goal_create,
                    single_task, task_create, task_delete, task_list, 
                    task_update)

urlpatterns = [
    # goal category urls
    path('categories/', categories_list, name='category-list'),
    path('category/<pk>/', single_category, name='category-detail'),
    path('category/<pk>/update/', category_update, name='category-update'),
    path('category/<pk>/delete/', category_delete, name='category-delete'),
    path('create-category/', category_create, name='category-create'),

    # goal urls
    path('', goal_dashboard, name='goal-dashboard'),
    path('goal/<pk>/', single_goal, name='goal-detail'),
    path('goal/<pk>/update/', goal_update, name='goal-update'),
    path('goal/<pk>/delete/', goal_delete, name='goal-delete'),
    path('create-goal/', goal_create, name='goal-create'),

    # goal task urls
    path('tasks/', task_list, name='task-list'),
    path('task/<pk>/', single_task, name='task-detail'),
    path('task/<pk>/update/', task_update, name='task-update'),
    path('task/<pk>/delete/', task_delete, name='task-delete'),
    path('create-task/', task_create, name='task-create'),
]