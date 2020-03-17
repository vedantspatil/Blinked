from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User as AuthUser
from blink.models import User
from django.contrib import messages


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

    print(request.POST)
    template = loader.get_template('blink/signup.html')

    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            AuthUser.objects.get(username=username)
            messages.error(request, 'This handle is currently in use')
            context = {
                'user': None,
            }
            print("no")
            return HttpResponse(template.render(context, request))

        except AuthUser.DoesNotExist:
            AuthUser.objects.create_user(username=username, password=password)
            User(username=username, password=password).save()
            print("yes")
            return HttpResponseRedirect("/")
    context = {
        'user': None,
    }
    return HttpResponse(template.render(context, request))
