from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone as dtz
# Create your models here.
class User(AbstractUser):
    email=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=255)
    followers=models.IntegerField(default=0)
    following=models.IntegerField(default=0)
    username=None
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    
    
    
class Post(models.Model):
    id=models.AutoField(primary_key=True)
    userid=models.ForeignKey(User,on_delete=models.CASCADE,to_field='id')
    title=models.TextField(max_length=100,default='')
    description=models.TextField(max_length=500,default='')
    time=models.DateTimeField(default=dtz.now())
    like=models.IntegerField(default=0)
    dislike=models.IntegerField(default=0)
    
class Comment(models.Model):
    id=models.AutoField(primary_key=True)
    postid=models.ForeignKey(Post,on_delete=models.CASCADE)
    like=models.IntegerField(default=0)
    dislike=models.IntegerField(default=0)
    time=models.DateTimeField(default=dtz.now())