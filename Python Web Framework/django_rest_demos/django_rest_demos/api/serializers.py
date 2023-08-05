from rest_framework import serializers as rest_serializers

from django_rest_demos.api.models import Employee, Department


# Same, but no department
class ShortEmployeeSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name']


# Same, but no employee
class ShortDepartmentSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DepartmentSerializer(rest_serializers.ModelSerializer):

    employee_set = ShortEmployeeSerializer(many=True)   # many=True because employee has more than 1 field

    class Meta:
        model = Department
        fields = '__all__'

def get_or_create_department_by_name(name):
    try:
        return Department.objects.filter(name=name).get()
    except Department.DoesNotExist:
        return Department.objects.create(name=name)


class EmployeeSerializer(rest_serializers.ModelSerializer):
    # GET:
    department = ShortDepartmentSerializer()

    class Meta:
        model = Employee
        fields = '__all__'

    # POST
    def create(self, validated_data):
        department_name = validated_data.pop('department').get('name')

        return Employee.objects.create(
            **validated_data,
            department=get_or_create_department_by_name(department_name),
        )


# class DepartmentSerializer(serializers.HyperlinkedModelSerializer):


class DepartmentNameSerializer(rest_serializers.Serializer):
    name = rest_serializers.CharField()


class DemoSerializer(rest_serializers.Serializer):
    employees = ShortEmployeeSerializer(many=True)
    departments = ShortDepartmentSerializer(many=True)

    employees_count = rest_serializers.IntegerField()
    first_department = rest_serializers.CharField()

    department_names = DepartmentNameSerializer(many=True)