from django.db import models
from users.models import User
from projects.constants import ROLE_CHOICES
# Create your models here.
# Store Project Data
class Project(models.Model):
  name = models.CharField(max_length=100)
  owner = models.ForeignKey(User,related_name="projects", on_delete=models.CASCADE)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.name} by {self.owner}"

ROLE_CHOICES = [
      ('Admin', 'Admin'),
      ('Member', 'Member'),
    ]
class ProjectMember(models.Model):
  project = models.ForeignKey(Project,related_name="members", on_delete=models.CASCADE)
  user = models.ForeignKey(User,related_name="projects_members", on_delete=models.CASCADE)
  role = models.CharField(max_length=10, choices=ROLE_CHOICES)
  def __str__(self):
    return f"{self.user.username} - {self.project.name} - {self.role}"