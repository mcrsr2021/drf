from testapp.models import Employee
from testapp.forms import EmployeeForm
from django.http import HttpResponse
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import View
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeDetail(View):
    def get(self,request,pk,*args,**kwargs):
        try:
            emp = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'The requested resource not available'})
            return HttpResponse(json_data,content_type='application/json',status=404)
        
        json_data = serialize('json',[emp,])
        p_data = json.loads(json_data)
        final_list = []
        for obj in p_data:
            emp_data = obj['fields']
            final_list.append(emp_data)
        json_data = json.dumps(final_list)
        return HttpResponse(json_data,content_type='application/json',status=200)

    def put(self,request,pk,*args,**kwargs):
        try:
            emp = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'The requested resource not available'})
            return HttpResponse(json_data,content_type='application/json',status=404)

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

    def delete(self,request,pk,*args,**kwargs):
        try:
            emp = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'The requested resource not available'})
            return HttpResponse(json_data,content_type='application/json',status=404)
        
        emp.delete()
        return HttpResponse(status=204)


@method_decorator(csrf_exempt,name='dispatch')
class EmployeeList(View):
    def get(self,request,*args,**kwargs):
        emp = Employee.objects.all()
        json_data = serialize('json',emp)
        p_data = json.loads(json_data)
        final_list = []
        for obj in p_data:
            emp_data = obj['fields']
            final_list.append(emp_data)
        json_data = json.dumps(final_list)
        return HttpResponse(json_data,content_type='application/json',status=200)

    def post(self,request,*args,**kwargs):
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
