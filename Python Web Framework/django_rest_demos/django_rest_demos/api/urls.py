from django.urls import path, include

from django_rest_demos.api.views import EmployeesListAPIView, DepartmentsAPIView, DemoAPIView, EmployeeViewSet

urlpatterns = (
    path('employees/', EmployeesListAPIView.as_view(), name='api employees'),
    path('departments/', DepartmentsAPIView.as_view(), name='api departments'),
    path('demo/', DemoAPIView.as_view(), name='api demo'),
    path('set/', EmployeeViewSet.as_view({'get': 'list'}), name='api set demo'),
)
