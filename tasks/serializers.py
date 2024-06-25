from rest_framework import serializers
from tasks.models import Task, Comments
from users.models import User
from users.serializers import UserDetailsSerializer
from projects.serializers import ProjectSerializer

class TaskSerializer(serializers.ModelSerializer):
  assigned_to = UserDetailsSerializer(read_only=True)
  assigned_to_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, write_only=True, source='assigned_to')

  # project = serializers.ReadOnlyField(source='project.id')
  project = ProjectSerializer(read_only=True)

  class Meta:
    model = Task
    fields = ['id', 'title', 'description', 'status', 'priority', 'assigned_to', 'assigned_to_id', 'project', 'created_at', 'due_date']
    extra_kwargs = {
      'id': {'read_only': True},
      'created_at': {'read_only': True},
    }

class CommentSerializer(serializers.ModelSerializer):
  user = UserDetailsSerializer(read_only=True)
  task = serializers.ReadOnlyField(source='task.id')

  class Meta:
    model = Comments
    fields = ['id', 'content', 'user', 'task', 'created_at']
    extra_kwargs = {
      'id': {'read_only': True},
      'created_at': {'read_only': True},
    }