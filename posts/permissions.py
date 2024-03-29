from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Only authenticated users can see the list
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD or OPTIONS requests to all
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Provide write permissions to the author of the post
        return obj.author == request.user # Here, obj is the object which is being accessed.