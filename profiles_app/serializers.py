from rest_framework import serializers
from profiles_app import models

class HelloSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=10)
        

class UserProfileSerializer(serializers.ModelSerializer):
    """serializes a user profile object"""
    
    class Meta:
        model=models.UserProfile
        fields=('id','name','email','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    def create(self, validated_data):
        """create and return a new user"""

        return models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
    

    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)