from api.models import Post,Comment,User
from api.serilizers import PostSerilizer,CommentSerilizer,UserLoginSerilizer
from rest_framework.response import Response
from rest_framework import generics,mixins
from rest_framework.exceptions import AuthenticationFailed
from django.db.models import F
import jwt,datetime
# Create your views here.    
    
class PostViewSet(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    serializer_class=PostSerilizer
    queryset=Post.objects.all()
    lookup_field='id'
    
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self,request):
        post=Post.objects.create(userid=request.user,title=request.data['title'],description=request.data['description'])
        post.save()
        return self.list(request)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        Post.objects.filter(id=id).delete()
        return self.list(request,id)
    
    
class PostViewSetLike(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    serializer_class=PostSerilizer
    queryset=Post.objects.all()
    lookup_field='id'
    
    def post(self,request,id=None):
        if id:
            post=Post.objects.get(id=id)
            post.like=post.like+1
            post.save()
            return self.list(request)
        else:
            return Response({'message':'id is getting none'})
    
class PostViewSetUnLike(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    serializer_class=PostSerilizer
    queryset=Post.objects.all()
    lookup_field='id'
    
    def post(self,request,id=None):
        if id:
            post=Post.objects.get(id=id)
            post.dislike=post.dislike+1
            post.save()
            return self.list(request)
        else:
            return Response({'message':'id is getting none'})
    

class CommentViewSet(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    serializer_class=CommentSerilizer
    queryset=Comment.objects.all()
    lookup_field='id'
    
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.delete(request,id)
    

class LoginViewSet(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    serializer_class=UserLoginSerilizer
    queryset=User.objects.all()
    lookup_field='id'
    
    def get(self,request,id=None):
        return self.retrieve(request,id)
    
    def get(self,request):
        email=request.data['email']
        password=request.data['password']
        user=User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        payload={
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }
        token=jwt.encode(payload,'secret',algorithm='HS256')
        response=Response()
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data={
            'jwt':token
        }
        return response
    
    def post(self,request):
        return self.create(request)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.delete(request,id)
    
    
class UserViewSet(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    serializer_class=UserLoginSerilizer
    queryset=User.objects.all()
    lookup_field='id'
    
    def get(self,request,id=None):
        print(id)
        return self.retrieve(request,id)
    
    
    def post(self,request,id=None):
        user1=User.objects.get(id=request.user.id)
        user2=User.objects.get(id=id)
        user1.followers=user1.followers+1
        user2.following=user2.following+1
        user1.save()
        user2.save()
        id=request.user.id
        return self.retrieve(request,id)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.delete(request,id)
    
    
class UserViewSett(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    serializer_class=UserLoginSerilizer
    queryset=User.objects.all()
    lookup_field='id'
    
    
    def post(self,request,id=None):
        user1=User.objects.get(id=request.user.id)
        user2=User.objects.get(id=id)
        user1.followers=user1.followers-1
        user2.following=user2.following-1
        user1.save()
        user2.save()
        id=request.user.id
        return self.retrieve(request,id)