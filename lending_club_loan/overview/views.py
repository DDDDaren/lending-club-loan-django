from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse('<p>home view</p>')

def loan_detail(request, id):
	return HttpResponse('<p>loan_detail view with id {}</p>'.format(id))