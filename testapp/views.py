from django.views.decorators import csrf
from testapp.models import Employee
from testapp.forms import EmployeeForm
from django.http import HttpResponse
from django.core.serializers import serialize
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
        json_data = serialize('json',[emp,])
        p_data = json.loads(json_data)
        final_list = []
        for obj in p_data:
            emp_data = obj['fields']
            final_list.append(emp_data)
        json_data = json.dumps(final_list)
        return HttpResponse(json_data,content_type='application/json',status=200)
    
    elif request.method == 'PUT':
        b_data = request.body  #binary data
        json_data = b_data.decode('utf-8') # json data
        try:
            p_data = json.loads(json_data) #python object
        except:
            json_data = json.dumps({'msg':'Please Provide data in valid json format'})
            return HttpResponse(json_data,content_type='application/json',status=400)
        from django.forms.models import model_to_dict
        original_data = model_to_dict(emp)
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
        json_data = serialize('json',emp)
        p_data = json.loads(json_data)
        final_list = []
        for obj in p_data:
            emp_data = obj['fields']
            final_list.append(emp_data)
        json_data = json.dumps(final_list)
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