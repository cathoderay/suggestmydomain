from django.shortcuts import render_to_response
from core import find_available


def home(request):
    return render_to_response('index.html')


def find(request):
    return render_to_response('domain.html', {'name': find_available()})
