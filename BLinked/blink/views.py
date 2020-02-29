from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def index(request):
    template = loader.get_template('blink/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('blink/login.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def signup(request):
    template = loader.get_template('blink/signup.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

