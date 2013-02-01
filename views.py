from django.shortcuts import render_to_response
from django.views.decorators.cache import never_cache

from core import find_available


@never_cache
def home(request):
    return render_to_response('index.html', {'name': find_available()})

