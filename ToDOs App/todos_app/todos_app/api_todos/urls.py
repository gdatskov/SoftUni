from django.urls import path

from todos_app.api_todos.views import ListCreateTodosAPIView, ListCategoriesAPIView, DetailsTodoAPIView

urlpatterns = [
    path('', ListCreateTodosAPIView.as_view(), name='create todos view'),
    path('categories/', ListCategoriesAPIView.as_view(), name='category view'),
    path('<int:pk>/', DetailsTodoAPIView.as_view(), name='details view'),
]
