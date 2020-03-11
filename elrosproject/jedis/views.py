from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("<h2>Hollou Jedis World</h2>")

def index(request):
    return HttpResponse("<h2>index</h2>")