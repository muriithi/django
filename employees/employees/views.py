from django.http import HttpResponse
from django.core import serializers
from employees.models import Employee

def employees(request):
	data = serializers.serialize('json', Employee.objects.all())
	return HttpResponse(data,mimetype = 'application/json')