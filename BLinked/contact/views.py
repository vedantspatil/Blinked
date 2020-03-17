from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def index(request):
    """
    Renders the contact Page

    :param request: request Object from Client
    :return: contact page
    """
    template = loader.get_template('contact/contact.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

