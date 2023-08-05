from django.shortcuts import render
from django.views import generic as generic_views
from rest_framework import \
    generics as rest_views, \
    serializers as rest_serializers, \
    viewsets as rest_viewsets
from rest_framework import views as rest_base_views
from rest_framework.response import Response

from django_rest_demos.api.models import Employee, Department
from django_rest_demos.api.serializers import EmployeeSerializer, DepartmentSerializer, ShortEmployeeSerializer, \
    ShortDepartmentSerializer, DemoSerializer


# Server-side rendering (result is rendered in HTML)
class EmployeesListView(generic_views.ListView):
    model = Employee
    template_name = ''


# JSON Serialization (parse models into JSON)
class EmployeesListAPIView(rest_views.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # Creating a query parameter functionality
    # e.g. http://127.0.0.1:8000/employees/?department_id=2
    def get_queryset(self):
        department_id = self.request.query_params.get('department_id')
        queryset = self.queryset
        if department_id:
            queryset = queryset.filter(department_id=department_id)
        return queryset.all()


class DepartmentsAPIView(rest_views.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DemoAPIView(rest_base_views.APIView):
    def get(self, request):
        body = {
            'employees': Employee.objects.all(),
            'employees_count': Employee.objects.count(),
            'departments': Department.objects.all(),
            'first_department': Department.objects.first(),
            'department_names': Department.objects.all(),  # not very different in this case, but useful for other cases
        }

        serializer = DemoSerializer(body)

        # DJANGO REST Response, not the standard Django HttpRequest
        return Response(serializer.data)


# ViewSets provide tools for all CRUD operations on MODEL SETS
class EmployeeViewSet(rest_viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
