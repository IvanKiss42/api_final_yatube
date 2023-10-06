from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Comment, Group, Follow
from .serializers import (PostSerializer, CommentSerializer, GroupSerializer,
                          FollowSerializer)
from .permissions import OnlyAuthorPutPatchDelete, FollowPermissions

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [OnlyAuthorPutPatchDelete]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        if self.request.data.get('group'):
            group_id = self.request.data.get('group')
            group = Group.objects.get(id=group_id)
            serializer.save(author=self.request.user,
                            group=group)
        else:
            serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [OnlyAuthorPutPatchDelete]
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        get_object_or_404(Post, id=post_id)
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        if serializer.is_valid():
            serializer.save(author=self.request.user,
                            post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    permission_classes = [FollowPermissions]
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        new_queryset = Follow.objects.filter(user=self.request.user)
        return new_queryset

    def perform_create(self, serializer):
        if serializer.is_valid(raise_exception=True):
            following_name = self.request.data.get('following')
            if type(following_name) is str:
                following = User.objects.get(username=following_name)
            elif type(following_name) is int:
                following = User.objects.get(id=following_name)
            else:
                raise NameError(
                    f'following name: {following_name} - and it is invalid'
                )
            serializer.save(user=self.request.user,
                            following=following)
