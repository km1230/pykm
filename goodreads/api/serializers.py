from rest_framework_json_api import serializers
from django.contrib.auth.models import User, Group
from .models import Book, Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'is_staff', 'groups']

    def create(self, validated_data):
        members = Group.objects.get(name="Members")
        u = User.objects.create(**validated_data)
        u.set_password(validated_data.get("password"))
        u.groups.add(members)
        u.save()
        return u