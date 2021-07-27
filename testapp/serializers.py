from testapp.models import Employee
from rest_framework import serializers


# class EmployeeSerializer(serializers.Serializer):
#     eno = serializers.IntegerField()
#     ename = serializers.CharField()
#     esal = serializers.FloatField()
#     eaddr = serializers.CharField(style={'base_template':'textarea.html'})

#     def create(self, validated_data):
#         return Employee.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.eno = validated_data.get('eno',instance.eno)
#         instance.ename = validated_data.get('ename',instance.ename)
#         instance.esal = validated_data.get('esal',instance.esal)
#         instance.eaddr = validated_data.get('eaddr',instance.eaddr)
#         instance.save()
#         return instance


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'