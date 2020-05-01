from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User as AuthUser
from blink.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as Login, logout as Logout
from passlib.hash import pbkdf2_sha256


def index(request):
    """
    renders index page of BLINKED

    :param request:
    :return: BLINKED page
    """
    template = loader.get_template('blink/index.html')
    context = {
        'page': 'Blinked',
        'user': request.user,
    }
    return HttpResponse(template.render(context, request))


def login(request):
    """
    logs in the client

    :param request: Request object from client
    :return: login page
    """
    template = loader.get_template('blink/login.html')
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            print("yes")
            Login(request, user)
            messages.success(request, "You are successfully logged in")
            return HttpResponseRedirect("/")
        else:  # invalid user so same page
            context = {
                'page': 'login',
                'user': user,
                'error': 'Invalid handle or password',
            }
            messages.error(request, 'Invalid username or password')
            return HttpResponse(template.render(context, request))

    context = {
        'page': 'login',
        'user': request.user,
    }
    return HttpResponse(template.render(context, request))


def signup(request):
    """
    registers the user

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
            encPassword = pbkdf2_sha256.encrypt(password, rounds=120000, salt_size=32)

            User(username=username, password=encPassword).save()
            messages.success(request, "You have successfully signed up")

            return HttpResponseRedirect("/")
    context = {
        'page': 'sign up',
        'user': request.user,
    }
    return HttpResponse(template.render(context, request))


def logout(request):
    """
    logs out the user
    :param request: Request object from client
    :return: index page
    """
    Logout(request)
    return HttpResponseRedirect("/")
