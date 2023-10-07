from rest_framework import permissions


class OnlyAuthorPutPatchDelete(permissions.IsAuthenticatedOrReadOnly):
    edit_methods = ('PUT', 'PATCH', 'DELETE')

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_superuser or obj.author == request.user)


class FollowPermissions(permissions.IsAuthenticated):
    edit_methods = ('POST',)

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.author == request.user
