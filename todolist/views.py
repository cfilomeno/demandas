from django.http import HttpResponse
from django.shortcuts import render
HttpResponse

def index(request):
    return HttpResponse("Este é o app todolist")
# Create your views here.
