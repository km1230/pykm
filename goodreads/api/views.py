from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer, UserSerializer
from rest_framework_json_api import views
from rest_framework import permissions, filters, decorators

# Create your views here.
class BookViewSet(views.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    search_fields = ['title', 'author']


class CategoryViewSet(views.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class PermittedUser(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        print(obj.username, request.user)        
        if (obj.username == request.user.username) or request.user.is_staff:
            return True
        else:
            return False


class UserViewSet(views.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [PermittedUser]
        return [permission() for permission in permission_classes]