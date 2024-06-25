from rest_framework import serializers
from projects.models import Project
from users.serializers import UserDetailsSerializer

class ProjectSerializer(serializers.ModelSerializer):
  owner = UserDetailsSerializer(read_only=True)
  class Meta:
    model = Project
    fields = ["id", "name", "description", "owner", "created_at"]
    extra_kwargs = {
      'id': {'read_only': True},
      'created_at': {'read_only': True},
      'owner': {'read_only': True},
    }