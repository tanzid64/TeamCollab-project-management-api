from rest_framework import serializers
from projects.models import Project, ProjectMember
from users.serializers import UserDetailsSerializer
from users.models import User

class ProjectSerializer(serializers.ModelSerializer):
  owner = UserDetailsSerializer(read_only=True)
  class Meta:
    model = Project
    fields = ["id", "name", "description", "owner", "created_at"]
    extra_kwargs = {
      'created_at': {'read_only': True},
      'owner': {'read_only': True},
    }


class ProjectMemberSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='user')
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = ProjectMember
        fields = ["id", "role", "user", "user_id", "project"]