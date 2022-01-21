from django.http import Http404, HttpRequest
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpRequest("Hello WOrld!")