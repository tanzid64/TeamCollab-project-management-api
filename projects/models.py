from django.db import models
from users.models import User
# Create your models here.
# Store Project Data
class Project(models.Model):
  name = models.CharField(max_length=100)
  owner = models.ForeignKey(User,related_name="projects", on_delete=models.CASCADE)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)