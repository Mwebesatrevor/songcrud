from rest_framework import permissions

class IsCreatorOrAdminReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    edit_methods = ('PUT','PATCH')

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user.is_staff and request.method not in self.edit_methods: # is_staff cannot PUT and PATCH info in the admin
            return True 

        if request.user.is_superuser: # superuser can do anything
            return True
        
        if request.user == obj: 
            return True

