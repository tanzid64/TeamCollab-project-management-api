from rest_framework import serializers
from users.models import User
from django.contrib.auth import authenticate

class UserRegisterSerializer(serializers.ModelSerializer):
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
  
class UserLoginSerializer(serializers.Serializer):
  email = serializers.EmailField(max_length=255)
  password = serializers.CharField(write_only=True)

  class Meta:
    model = User
    fields = ['email', 'password']

  def validate(self, data):
    email = data.get('email')
    password = data.get('password')
    
    # Using `username` field for authentication as the default User model does not have an email field for authentication
    user = authenticate(username=email, password=password)
    
    if not user:
      raise serializers.ValidationError('Incorrect Credentials')
    
    data['user'] = user
    return data
  
class UserDetailsSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'first_name', 'last_name']
    