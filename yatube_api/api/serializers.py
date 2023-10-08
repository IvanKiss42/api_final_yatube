from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, PrimaryKeyRelatedField

from posts.models import Comment, Post, Group, Follow


User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        required=True
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate(self, attrs):
        if self.context['request'].user == attrs['following']:
            raise ValidationError(
                "User can't be self suscribed"
            )
        if Follow.objects.filter(
            user=self.context['request'].user,
            following=User.objects.get(username=attrs['following'])
        ):
            raise ValidationError("This following already exists")
        if attrs['following'] is None:
            raise ValidationError("Required field")
        return attrs
