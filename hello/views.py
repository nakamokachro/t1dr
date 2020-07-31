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
        answer = main(query)
        html = ("<H1>I will tl;dr this for you:</H1>" + answer)
        return HttpResponse(html)
    else:
        return render(request, 'form.html')
    

def main(query):
    return query.upper()
