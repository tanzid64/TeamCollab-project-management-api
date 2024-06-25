from django.urls import path, include
from rest_framework import routers
from projects.views import ProjectViewSet, ProjectMemberViewSet
# Create a router for ProjectViewSet
project_router = routers.DefaultRouter()
project_router.register(r'', ProjectViewSet, basename='project-api')

# Create a router for ProjectMemberViewSet, nested under projects
member_router = routers.DefaultRouter()
member_router.register(r'members', ProjectMemberViewSet, basename='project-member-api')

# Include both routers in urlpatterns
urlpatterns = [
    path('', include(project_router.urls)),
    path('<int:project_id>/', include(member_router.urls)),
]
