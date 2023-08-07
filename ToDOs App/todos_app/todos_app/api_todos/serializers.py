from rest_framework import serializers as rest_serializers

from todos_app.api_todos.models import Todo, Category


class TodoListSerializer(rest_serializers.ModelSerializer):
    class Meta:
        # fields = '__all__'
        fields = ('id', 'title',)
        model = Todo


class TodoCreateSerializer(rest_serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        # fields = ('id', 'title', 'description', 'category')
        model = Todo


class CategorySerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class TodoDetailsSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
