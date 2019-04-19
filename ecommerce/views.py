from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	context ={
		"name": "Masum Bin Alam",
		"age" : "23"
	}
	return render(request, "homepage.html", context)

def about(request):
	context ={
		"name": "Masum Bin Alam",
		"age" : "23"
	}
	return render(request, "about.html", context)