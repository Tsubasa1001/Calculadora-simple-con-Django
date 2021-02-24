import json

from django.http import HttpResponse
from django.shortcuts import render

from . import calculator

# Create your views here.
def index(request):
	return render(request, 'calculadora/index.html', {})

def prefix(request):
	expression = __add_sum_value(request.GET.get('expression'))
	expression = {'data': calculator.InfixToPrefix(expression), 'method': "prefix"}
	return HttpResponse(json.dumps(expression), content_type='application/json')

def postfix(request):
	expression = __add_sum_value(request.GET.get('expression'))
	expression = {'data': calculator.InfixToPostfix(expression), 'method': "postfix"}
	return HttpResponse(json.dumps(expression), content_type='application/json')

def tree(request):
	expression = __add_sum_value(request.GET.get('expression'))
	expression = {'data': calculator.main_tree(expression), 'method': "tree"}
	return HttpResponse(json.dumps(expression), content_type='application/json')

def __add_sum_value(expression):
	return expression.replace(" ", "+")