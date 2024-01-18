from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_description = models.TextField(max_length=1000,null=True,blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.task_name

    class Meta:
        ordering = ['status']
