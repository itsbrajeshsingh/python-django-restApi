from django.urls import path,include
from .views import PostViewSet,CommentViewSet,LoginViewSet,UserViewSet,UserViewSett,PostViewSetLike,PostViewSetUnLike

urlpatterns = [
    path("user/",UserViewSet.as_view()),
    path("user/<int:id>/",UserViewSet.as_view()),
    path("follow/<int:id>/",UserViewSet.as_view()),
    path("unfollow/<int:id>/",UserViewSett.as_view()),
    path("posts/allposts",PostViewSet.as_view()),
    path("posts/<int:id>",PostViewSet.as_view()),
    path("like/<int:id>",PostViewSetLike.as_view()),
    path("unlike/<int:id>",PostViewSetUnLike.as_view()),
    path("comment/<int:id>",PostViewSet.as_view()),
    path("authenticate/",LoginViewSet.as_view()),
    path("authenticate/",LoginViewSet.as_view()),
]
