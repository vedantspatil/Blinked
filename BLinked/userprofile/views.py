from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader



def index(request, username):
    """
    Renders the user profile page

    :param request: request from client
    :param username: username of the profile page
    :return: user profile page
    """

    template = loader.get_template('userprofile/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

