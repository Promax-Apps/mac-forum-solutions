from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hi there")


def say_hello(request, name=None):
    return HttpResponse(f"Hello {name}")
