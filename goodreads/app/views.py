from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer, UserSerializer
from rest_framework_json_api.views import ModelViewSet
from rest_framework import permissions

# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # add user to Reader group automatically
    def create(self):
        return self.groups.add('Members')