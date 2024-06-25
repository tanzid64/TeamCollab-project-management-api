from django.db import models
from users.models import User
from projects.models import Project
from tasks.constants import STATUS_CHOICES, PRIORITY_CHOICES
# Create your models here.
class Task(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  status = models.CharField(max_length=20, choices=STATUS_CHOICES)
  priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
  assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  due_date = models.DateTimeField()

  def __str__(self):
    return self.title
  
class Comments(models.Model):
  content = models.TextField()
  user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
  task = models.ForeignKey(Task, related_name="comments", on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return f"Comment by {self.user.username} on {self.task.title}"