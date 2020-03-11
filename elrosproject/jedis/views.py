from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Planet, Jedi, Candidate, Tests,  Questions

# Create your views here.
def index(request):
    return render(request, 'jedis/index.html', {'foo': 'bar'})


def get_jedi(request):
    return render(request, 'jedis/index.html', {'foo': 'bar'})


def get_candidate(request):
    return render(request, 'jedis/index.html', {'foo': 'bar'})
