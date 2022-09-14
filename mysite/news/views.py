# Create your views here.
from django.http import HttpResponse


def index(request):
    # print(request)
    return HttpResponse('Hello world')


def test(request):
    return HttpResponse('<h1>Test page</h1>')
