from rest_framework import serializers
from api.models import  Comment, Post,User

class UserLoginSerilizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','followers','following']
    def create(self, validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        
class PostSerilizer(serializers.ModelSerializer):
    userid=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=Post
        fields=['id','userid','title','description','like','dislike']
        
class CommentSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields="__all__"