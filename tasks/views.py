from rest_framework import generics, permissions
from tasks.models import Task, Comments
from tasks.serializers import TaskSerializer, CommentSerializer
from tasks.permissions import IsTaskCreateAllowed, IsCommentPostAllowed, IsCommentOwnerOrAdmin,IsTaskUpdateAllowed

class TaskListCreateView(generics.ListCreateAPIView):
  serializer_class = TaskSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsTaskCreateAllowed]

  def get_queryset(self):
    return Task.objects.filter(project_id=self.kwargs['project_id'])

  def perform_create(self, serializer):
    project_id = self.kwargs['project_id']
    serializer.save(project_id=project_id)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
  permission_classes = [ IsTaskUpdateAllowed,]

class CommentListCreateView(generics.ListCreateAPIView):
  serializer_class = CommentSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCommentPostAllowed]

  def get_queryset(self):
    return Comments.objects.filter(task_id=self.kwargs['task_id'])

  def perform_create(self, serializer):
    task_id = self.kwargs['task_id']
    serializer.save(task_id=task_id, user=self.request.user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Comments.objects.all()
  serializer_class = CommentSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCommentOwnerOrAdmin]
