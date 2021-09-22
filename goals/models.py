from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=45)
    url = models.SlugField(max_length=250)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category-detail', kwargs={
            'pk': self.url
        })

    def get_update_url(self):
        return reverse('category-update', kwargs={
            'pk': self.url
        })

    def get_delete_url(self):
        return reverse('category-delete', kwargs={
            'pk': self.url
        })


class Goal(models.Model):
    status_choices = (
        ('in-progress', 'In-Progress'),
        ('completed', 'Completed'),
    )
    created_date = models.DateTimeField(auto_now_add=True)
    target_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    url = models.SlugField(max_length=250)
    goal = models.CharField(max_length=300)
    specific = models.TextField()
    measurable = models.TextField()
    achievable = models.TextField()
    relevant = models.TextField()
    timely = models.TextField()
    category = models.ForeignKey(Category, 
                                default=1, 
                                verbose_name='Category', 
                                on_delete=models.SET_DEFAULT)
    status = models.CharField(
        max_length=25, choices=status_choices, default='in-progress')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.goal

    def get_absolute_url(self):
        return reverse('goal-detail', kwargs={
            'pk': self.url
        })

    def get_update_url(self):
        return reverse('goal-update', kwargs={
            'pk': self.url
        })

    def get_delete_url(self):
        return reverse('goal-delete', kwargs={
            'pk': self.url
        })


class Task(models.Model):
    task = models.CharField(max_length=200)
    url = models.SlugField(max_length=250)
    due = models.DateField()
    description = models.TextField()
    completed = models.BooleanField()
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={
            'pk': self.url
        })

    def get_update_url(self):
        return reverse('task-update', kwargs={
            'pk': self.url
        })

    def get_delete_url(self):
        return reverse('task-delete', kwargs={
            'pk': self.url
        })
