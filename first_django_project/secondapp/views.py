from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
	print('hello')
	print('This msg will be displayed to the console')
	s = '<h1> Welcome to the web development world, You can create wonders here....</h1>'
	return HttpResponse(s)
