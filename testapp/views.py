from django.views.decorators import csrf
from testapp.models import Employee
from testapp.forms import EmployeeForm
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def employee_detail(request,pk):
    try:
        emp = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        json_data = json.dumps({'msg':'The requested resource not available'})
        return HttpResponse(json_data,content_type='application/json',status=404)
    if request.method == 'GET':
        emp_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr
        }
        json_data = json.dumps(emp_data)
        return HttpResponse(json_data,content_type='application/json',status=200)
    
    elif request.method == 'PUT':
        b_data = request.body  #binary data
        json_data = b_data.decode('utf-8') # json data
        try:
            p_data = json.loads(json_data) #python object
        except:
            json_data = json.dumps({'msg':'Please Provide data in valid json format'})
            return HttpResponse(json_data,content_type='application/json',status=400)
        original_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr
        }
        original_data.update(p_data)
        form = EmployeeForm(original_data)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg':'Record updated successfully'})
            return HttpResponse(json_data,content_type='application/json')
        if form.errors:
            json_data = json.dumps(form.errors)
            return HttpResponse(json_data,content_type='application/json',status=400)
    elif request.method == 'DELETE':
        emp.delete()
        return HttpResponse(status=204)

@csrf_exempt
def employee_list(request):
    if request.method == 'GET':
        emp = Employee.objects.all()
        emp_data = []
        for e in emp:
            e = {
                'eno':e.eno,
                'ename':e.ename,
                'esal':e.esal,
                'eaddr':e.eaddr
                }
            emp_data.append(e)
        json_data = json.dumps(emp_data)
        return HttpResponse(json_data,content_type='application/json',status=200)
    elif request.method == 'POST':
        b_data = request.body  #binary data
        json_data = b_data.decode('utf-8') # json data
        try:
            p_data = json.loads(json_data) #python object
        except:
            json_data = json.dumps({'msg':'Please Provide data in valid json format'})
            return HttpResponse(json_data,content_type='application/json',status=400)
        form = EmployeeForm(p_data)
        if form.is_valid():
            form.save()
            return HttpResponse(json_data,content_type='application/json',status=201)
        if form.errors:
            json_data = json.dumps(form.errors)
            return HttpResponse(json_data,content_type='application/json',status=400)
        