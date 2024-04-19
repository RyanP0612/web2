from django.shortcuts import render
from .models import * 
from .serializers import * 

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission
# Create your views here.
from django.core.exceptions import PermissionDenied
from django.db.models import Q

# class DeadlineCustomPermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.groups.filter(name='Coordenador').exists()

# class DeadlineCustomPermission(BasePermission):
#     def has_permission(self, request, view):
#         if request.method == 'GET':
#             return request.user.is_authenticated
#         return request.user.groups.filter(Q(name='Coordenador')|Q(name='Admin')).exists()
    
class DeadlineCustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user('main.view_deadline')
        return request.user.has_perms(['main.add_deadline', 'main.delete_deadline', 'main.change_deadline'])



class DeadlineView(ModelViewSet):
    queryset = Deadline.objects.all()
    serializer_class = DeadlineSerializer
    permission_classes = (DeadlineCustomPermission,)
