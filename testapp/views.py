from django.http import HttpResponse
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def employee_list(request):

    if request.method == 'GET':
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        emp = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=emp)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def employee_detail(request,pk):
    try:
        emp = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EmployeeSerializer(emp)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(emp,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)

    elif request.method == 'DELETE':
        emp.delete()
        return HttpResponse(status=204)

