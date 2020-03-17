from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def index(request):
    """
    renders index page of BLINKED

    :param request:
    :return: BLINKED page
    """
    template = loader.get_template('blink/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def login(request):
    """
    renders login page and logs in the client

    :param request: Request object from client
    :return: login page
    """
    template = loader.get_template('blink/login.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def signup(request):
    """
    renders sign up page and registers the user

    :param request: Request object from client
    :return: sign up page
    """
    template = loader.get_template('blink/signup.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
