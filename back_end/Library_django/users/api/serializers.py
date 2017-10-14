from rest_framework import serializers

from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        
        extra_kwargs = {
                'password': {'write_only': True}
        } 
        
    def create(self, validated_data):
        
        first_name = validated_data['first_name']
        last_name  = validated_data['last_name']
        username   = validated_data['username']
        email      = validated_data['email']
        password   = validated_data['password']
        
        user_obj = User(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email
        )
        user_obj.set_password(password)
        user_obj.save()
        
        return validated_data
        
#............................................................................................................
class UserLoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'password',)
        
        extra_kwargs = {
                'password': {'write_only': True}
        }
        
        
        
        
        
        
        
        
