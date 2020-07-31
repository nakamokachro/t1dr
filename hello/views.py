from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):
    if request.method == 'POST':
        query = request.POST.get('textfield', None)
        html = ("<H1>I will tl;dr this for you:</H1>" + query)
        return HttpResponse(html)
    else:
        return render(request, 'form.html')
