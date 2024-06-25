from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
  confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)

  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'password', 'confirm_password']
    extra_kwargs = {
      'password': {'write_only': True}
    }

  def create(self, validated_data):
    password = validated_data.pop('password', None)
    confirm_password = validated_data.pop('confirm_password', None)
    instance = self.Meta.model(**validated_data)
    if password != confirm_password:
      raise serializers.ValidationError({'password': 'Passwords do not match'})
    instance.set_password(password)
    instance.save()
    return instance