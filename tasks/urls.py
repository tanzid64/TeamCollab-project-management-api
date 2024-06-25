from django.urls import path
from .views import TaskListCreateView, TaskDetailView, CommentListCreateView, CommentDetailView

urlpatterns = [
    path('projects/<int:project_id>/tasks/', TaskListCreateView.as_view(), name='task-list-create-api'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail-api'),
    path('tasks/<int:task_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create-api'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail-api'),
]
