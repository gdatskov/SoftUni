from django.shortcuts import render
from django.views import generic as django_views
from rest_framework import generics as rest_views
from rest_framework import permissions, exceptions as rest_exceptions

from todos_app.api_todos.models import Todo, Category
from todos_app.api_todos.serializers import TodoCreateSerializer, TodoListSerializer, CategorySerializer, \
    TodoDetailsSerializer


class ListCreateTodosAPIView(rest_views.ListCreateAPIView):
    queryset = Todo.objects.all()

    # NOT BUILTIN - MUST OVERRIDE get_serializer_class method
    create_serializer_class = TodoCreateSerializer
    list_serializer_class = TodoListSerializer

    filter_names = ('category',)

    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        queryset = self.queryset.filter(category__user=self.request.user)

        # category_id = self.request.query_params.get('category', None)
        # if category_id:
        #     queryset = queryset.filter(category_id=category_id)

        # Apply filter dynamically:
        queryset = self.__apply_filters_to_queryset(queryset)
        return queryset

    def __apply_filters_to_queryset(self, queryset):
        queryset_params = {}
        for filter_name in self.filter_names:
            filter_id = self.request.query_params.get(filter_name, None)
            if filter_id:
                queryset_params[f'{filter_name}'] = filter_id
        return queryset.filter(**queryset_params)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.list_serializer_class
        return self.create_serializer_class     # if method = POST


class ListCategoriesAPIView(rest_views.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset


class DetailsTodoAPIView(rest_views.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoDetailsSerializer

    # Check if the user is owner
    # (url tampering)
    def get_object(self):
        obj = super().get_object()

        if obj.user != self.request.user:
            raise rest_exceptions.PermissionDenied

        return obj
