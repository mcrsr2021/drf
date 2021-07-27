from testapp.models import Employee
from rest_framework import serializers
from django.contrib.auth.models import User


class EmployeeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Employee
        fields = ['eno','ename','esal','eaddr','owner']


class UserSerializer(serializers.ModelSerializer):
    testapp = serializers.PrimaryKeyRelatedField(many=True,queryset=Employee.objects.all())

    class Meta:
        model = User
        fields = ['id','username','testapp']